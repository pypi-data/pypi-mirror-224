from typing import (
    Any,
    Dict,
    List,
    Optional,
    Set,
    Union,
)

from mlopscfg import struct_log
from mlopscfg.backend import (
    Backend,
    SSMParameterStore,
)


class MissingParameterError(Exception):
    """Class to wrap the exception when the parameter doesnt exists in the
    Backend."""

    def __init__(self, parameter_names: List[str], parameter_path: str, *args: object) -> None:
        super().__init__(*args)
        self.msg: str = f"Missing parameters {parameter_names} on path {parameter_path}"
        self.parameter_names: List[str] = parameter_names
        self.parameter_path: str = parameter_path


class InvalidParametersError(Exception):
    """Class to wrap exceptions on errors from the Backend."""

    def __init__(self, invalid_parameters: List[str]) -> None:
        self.invalid_parameters: List[str] = invalid_parameters
        self.msg: str = f"Invalid parameters {self.invalid_parameters} requested"


class Parameters:
    """Abstracts common operation on the Backend."""

    def __init__(self, backend: Optional[Backend] = None):
        self.backend = backend or SSMParameterStore()
        self.logger = struct_log.get_logger(name=self.__class__.__name__, level=struct_log.DEBUG, verbose=True)

    def get_parameters(self, keys: List[str]) -> Dict[str, Optional[str]]:
        """Retrieve keys from Backend. The keys are mapped to a dictionary for
        easy querying:

            * Keys that exist in the Backend should have a matching key in the result dict
              and a matching value.
            * Keys that do not exist in the Backend should also have a matching key, but
              have a matching value of None.

        If the Backend somehow returns keys that are not requested, these keys are not
        returned in the result dict.

        :param Keys: List
        :type Keys: list(str)
        :returns: Dict
        :raises InvalidParametersError: when invalid parameters were requested
        """

        response: Dict = self.backend.get_parameters(keys=keys)
        if response.get("InvalidParameters"):
            raise InvalidParametersError(response["InvalidParameters"])

        retrieved_parameters: List[Dict] = response.get("Parameters", [])

        # Initialise the result so that missing keys have a None value.
        filled_parameters: Dict[str, Optional[str]] = {parameter_name: None for parameter_name in keys}

        # Merge the retrieved parameters in.
        for retrieved in retrieved_parameters:
            if retrieved.get("Name") in keys:
                filled_parameters[retrieved["Name"]] = retrieved.get("Value")

        return filled_parameters

    def get_parameters_by_path(
        self,
        base_path: str,
        recursive: bool = True,
        nested: bool = True,
        required_parameters: Optional[Set[str]] = None,
    ) -> Dict[str, Union[Dict, Optional[str]]]:
        """Retrieve all the keys under a certain path and joins them under a
        json object.

        :param str base_path:  Root of the path to get values from

        :param recursive:
            * When recursive is set to False, the Backend doesn't return keys under a nested path.
                    e.g.: /{base_path}/foo/bar will not return 'bar' nor '/foo/bar'.
            * When recursive and nested are set to True, a nested dictionary is returned.
                            e.g.: /{base_path}/foo/bar will return {"foo": {"bar": "value"}}
        :type Recursive: bool

        :param required_parameters:
            * A set of required parameters. Before the parameters
              are processed, we assert that the required parameters are returned on this path.
            * We assert the parameters before transforming the parameters to a nested
              structure. Provide paths in path format, e.g. "foo/bar" for "/path/sub/foo/bar",
              to prevent your required path from being listed as missing
        :type required_parameters: list(str)

        :returns:
            * If nested=False, a dictionary of string to optional string value.
            * If nested=True, a dictionary of string to potentially nested dictionaries with
              optional string values.
        :rtype: dict
        """

        parameters = self.backend.get_parameters_by_path(path=base_path, recursive=recursive)

        parameters = {parameter.get("Name").replace(base_path, ""): parameter.get("Value") for parameter in parameters}

        if required_parameters:
            self._assert_required(required_parameters, parameters, base_path)
        return (
            # Non-nested is the default behaviour (hence `else parameters`).
            self._parse_parameters(parameters)
            if recursive and nested
            else self._strip_leading_slashes(parameters)
        )

    @staticmethod
    def _parse_parameters(parameters: Dict[str, Optional[str]]) -> Dict[str, Union[Dict, Optional[str]]]:
        """Build a nested dictionary based on the key by treating it as a path,
        ie:

        {'/foo/bar/koo': 42} returns { 'foo': { 'bar': { 'koo': 42 } } }
        :param parameters:
        :type parameters: dict(str,str)
        :returns: A nested dictionary based on the key delmited by '/'
        :rtype: dict
        """
        parsed_dict: Dict[str, Union[Dict, Optional[str]]] = {}
        for key, value in parameters.items():
            nested_dict = Parameters._tree_dict(key.split("/"), value)
            parsed_dict = Parameters._deep_merge(parsed_dict, nested_dict)
        return parsed_dict

    @staticmethod
    def _strip_leading_slashes(parameters: Dict[str, Optional[str]]) -> Dict[str, Union[Dict, Optional[str]]]:
        """Removes slashes from all the keys on a dictionary.

        :param parameters:
        :type parameters: dict(str,str)
        :returns: The dictionary without the slashes on the keys
        :retval: dict
        """
        return {parameter_key.lstrip("/"): parameter_value for parameter_key, parameter_value in parameters.items()}

    @staticmethod
    def _tree_dict(key_list: List[Any], value: Optional[Any]) -> Dict[Any, Any]:
        """Build a nested dictionary path from a list of keys and a value.

        Example::

            _tree_dict(["foo", "bar", "koo"], 42) ==>
            {"foo": {"bar": {"koo": 42}}}

        :param key_list: Source dictionary
        :type key_list: list
        :param value: Values
        :type value: list
        :returns: The nested dictionary
        :rtype: dict
        """
        tree_dict: Dict[Any, Any] = {key_list[-1]: value}
        for key in reversed(key_list[:-1]):
            tree_dict = {key: tree_dict}
        return tree_dict

    @staticmethod
    def _deep_merge(a: Union[Dict, Any], b: Union[Dict, Any]) -> Union[Dict, Any]:
        """Deep merge two dictionaries.

        :param a: First dictionary
        :type a: dict
        :param b: Second dictionary
        :type b: dict
        :returns: A dictionary that is the result merging both sources
        :rtype: dict
        """
        # NOTE: Thanks to: https://stackoverflow.com/a/56177639/9563578
        if not isinstance(a, dict) or not isinstance(b, dict):
            return a if b is None else b
        else:
            keys = set(a.keys()) | set(b.keys())
            return {key: Parameters._deep_merge(a.get(key), b.get(key)) for key in keys}

    @staticmethod
    def _assert_required(
        required_parameters: Set[str],
        actual_parameters: Dict[str, Any],
        parameter_path: str,
    ) -> None:
        """Assert that a set of required parameters exists as keys on a
        dictionary.

        :param required_parameters: A set of required parameters
        :type required_parameters: set(str)
        :param actual_parameters: A dictionary to test
        :type actual_parameters: dict(str,any)
        :param str parameter_path: Informative string to pass on the
            exception
        :raises MissingParameterError: If a parameter was not found as a
            key
        """
        missing_parameters: List[str] = [
            parameter_name for parameter_name in required_parameters if parameter_name not in actual_parameters
        ]
        if missing_parameters:
            raise MissingParameterError(missing_parameters, parameter_path)

    def put_parameter(
        self,
        path: str,
        value: str,
        overwrite: bool = False,
        tags: Optional[List[Dict[str, str]]] = None,
    ) -> Dict:
        """Stores a value in a path. A function to store a Value under a Name.

        :param str Path: Name of the Parameter
        :param Overwrite: if False it will generate an exception if the
            Parameter exists
        :type Overwrite: bool
        :param Tags: Tags to be added to the resource
        :type Tags: list(dict)
        :param Value: str:
        :rtype: Dict
        """
        return self.backend.put_parameter(
            name=path,
            value=value,
            overwrite=overwrite,
            tags=tags or [],
        )
