import contextlib
from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Dict,
    List,
    Optional,
)

import boto3

from mlopscfg import struct_log


class ExceptionLogger(contextlib.AbstractContextManager):
    """Class to catch an exception and loggit with our structured logger."""

    def __init__(self, class_name) -> None:
        super().__init__()
        self.logger = struct_log.get_logger(name=class_name, level=struct_log.DEBUG, verbose=True)

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.logger.exception(f"An error occurred while getting a parameter: {exc_value}")


class Backend(ABC):
    """Abstract class to define operations on a backend."""

    @abstractmethod
    def get_parameters(self, keys: List) -> Dict:
        """

        :param Keys: List of keys to get values
        :type Keys: list(str)

        """
        pass

    @abstractmethod
    def get_parameters_by_path(self, path: str, recursive: bool) -> Dict:
        """

        :param str Path: Path of the top level key to get values from
        :param bool Recursive: Retrieve all keys from the top or just the first one

        """
        pass

    @abstractmethod
    def put_parameter(self, name: str, value: str, overwrite: bool, tags: Dict) -> Dict:
        """

        :param str Name: Name of the key to store the value under
        :param str Value: Value to store
        :param Overwrite: If true and the key exists return an error
        :param Tags: A dictionary with key values of tags to asociate the parameter with
        :type Tags: dict(str,str)

        """
        pass

    @abstractmethod
    def delete_parameters(self, keys: List) -> Dict:
        """

        :param Keys:
        :type Keys: list(str)

        """
        pass

    @abstractmethod
    def delete_parameters_by_path(self, path: str) -> None:
        """

        :param str Path:

        """
        pass


class SSMParameterStore(Backend):
    """Backend class that implements the SSM Parameter store as storage for the
    configuration.

    The boto exception CLientError is going to be caught , logged with
    the structured logger and then released to be handled by the upper
    layers.
    """

    def __init__(
        self,
        client: Optional[boto3.client] = None,
        decrypt: Optional[bool] = False,
    ):
        """Constructor.

        Args:
        :param client: A boto3 client if None one will be created
        :type client: boto3.client
        :param decrypt: if True decrypt using KMS automatically
                        before returning/storing a value only used if SecureString
                        is implemented
        :type decrypt: bool
        """
        self.client = client or boto3.client("ssm")
        self.decrypt = decrypt
        self.logger = struct_log.get_logger(name=self.__class__.__name__, level=struct_log.DEBUG, verbose=True)

    def get_parameters(self, keys: List) -> Dict:
        """Takes a list of Keys and returns its values.

        :param Keys: A list of keys to retrieve values from the backend
        :type Keys: list(str)
        :returns: A dictionary with 2 lists, 'Parameters' and
            'InvalidParameters'
        :rtype: Dict
        """
        with ExceptionLogger(self.__class__.__name__):
            response = self.client.get_parameters(Names=keys, WithDecryption=self.decrypt)
            return {
                "Parameters": response.get("Parameters"),
                "InvalidParameters": response.get("InvalidParameters"),
            }

    def get_parameters_by_path(self, path: str, recursive: bool = True) -> Dict:
        """Retrieve all the keys under a certain path.

        :param Path: A string that points to the root of a tree of
            Parameters
        :type Path: str
        :param Recursive: Retrieve all parameters under the root
        :type Recursive: bool
        :returns: List of Dictionaries
        :rtype: Dict
        """

        with ExceptionLogger(self.__class__.__name__):
            return self.client.get_parameters_by_path(
                Path=path,
                Recursive=recursive,
                WithDecryption=self.decrypt,
            ).get("Parameters")

    def put_parameter(
        self,
        name: str,
        value: str,
        overwrite: bool = False,
        tags: Optional[List] = None,
    ) -> Dict:
        """A function to store a Value under a Name.

        :param Name: Name of the Parameters
            Naming Constraints:

            * Parameter names are case sensitive.
            * A parameter name cant include spaces.
            * A parameter name must be unique within an the AWS Region
            * A parameter name cant be prefixed with “aws” or “ ssm” (case-insensitive).
            * Parameter names can include only the following symbols and letters `a-zA-Z0-9_.-`
              In addition, the slash character ( / ) is used to delineate hierarchies in parameter names.
              For example: /Dev/Production/East/Project-ABC/MyParameter
            * Parameter hierarchies are limited to a maximum depth of fifteen levels.
        :type Name: str
        :param Overwrite: if False it will generate an exception if the Parameter exists
        :type Overwrite: bool
        :param Tags: Tags to be added to the resource
        :type Tags: list(dict)
        :param str Value:
        :returns: Output from the backend operation
        :rtype: Dict
        """
        with ExceptionLogger(self.__class__.__name__):
            return self.client.put_parameter(
                Name=name,
                Value=value,
                Type="String",
                Overwrite=overwrite,
                Tags=tags if tags else [],
                Tier="Standard",
            )

    def delete_parameters(self, keys: List) -> Dict:
        """Deletes a list of parameters from the store.

        :param Keys: List of Parameters to delete
        :type Keys: list(str)
        :returns: Dictionary with a DeletedParameters and
            InvalidParameters dictionaries.
        :rtype: Dict
        """
        with ExceptionLogger(self.__class__.__name__):
            response = self.client.delete_parameters(Names=keys)
            return {
                "DeletedParameters": response.get("DeletedParameters"),
                "InvalidParameters": response.get("InvalidParameters"),
            }

    def delete_parameters_by_path(self, path: str) -> Dict:
        """Function to manage paging when deleting parameters from a Path.

        :param str Path:
        :returns: same as
        :func: delete_parameters
        :rtype: Dict
        """
        with ExceptionLogger(self.__class__.__name__):
            # Creates a paginator and queries for a Path
            paginator = self.client.get_paginator("get_parameters_by_path")
            response_pages = paginator.paginate(
                Path=path,
                Recursive=True,
                WithDecryption=self.decrypt,
            )

            # Extracts the Parameters key from every page and deletes them
            names = []
            for response_page in response_pages:
                names.extend([p["Name"] for p in response_page.get("Parameters", [])])

            if names:
                return self.delete_parameters(keys=names)
            return {}
