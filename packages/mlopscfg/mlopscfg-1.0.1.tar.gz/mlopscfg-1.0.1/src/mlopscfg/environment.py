from __future__ import annotations

import json
from dataclasses import dataclass
from typing import (
    Dict,
    List,
)

from mlopscfg.parameters import Parameters


@dataclass(frozen=True)
class Account:
    """This class will describe the properties of an Account and must match the
    schema in the metadata store."""

    account_id: str
    env_prefix: str
    account_name: str
    sagemaker_kms_key_id: str

    @staticmethod
    def from_dict(obj: Dict) -> Account:
        """This method will create an Account object from a dictionary.

        :param obj: Dictionary that must contain the properties of the
            Account
        :type obj: Dict
        :return: An Account object
        :rtype: Account
        """
        _account_id = str(obj.get("account_id"))
        _env_prefix = str(obj.get("env_prefix"))
        _account_name = str(obj.get("account_name"))
        _sagemaker_kms_key_id = str(obj.get("sagemaker_kms_key_id"))
        return Account(_account_id, _env_prefix, _account_name, _sagemaker_kms_key_id)


# Services
@dataclass(frozen=True)
class GlueCrawlersInputs:
    glue_crawler_connection_name: str
    model_output_database_name: str

    @staticmethod
    def from_dict(obj: Dict) -> GlueCrawlersInputs:
        _glue_crawler_connection_name = str(obj.get("glue_crawler_connection_name"))
        _model_output_database_name = str(obj.get("model_output_database_name"))
        return GlueCrawlersInputs(_glue_crawler_connection_name, _model_output_database_name)


@dataclass(frozen=True)
class Networking:
    subnet_ids: List[str]
    vpc_endpoint_sg_id: str
    vpc_id: str

    @staticmethod
    def from_dict(obj: Dict) -> Networking:
        _subnet_ids = obj.get("subnet_ids")
        _vpc_endpoint_sg_id = str(obj.get("vpc_endpoint_sg_id"))
        _vpc_id = str(obj.get("vpc_id"))
        return Networking(_subnet_ids, _vpc_endpoint_sg_id, _vpc_id)


# Class Wrappers
@dataclass(frozen=True)
class Accounts:
    dev_application: Account
    exploration: Account
    prod: Account
    shared_services: Account
    staging: Account

    @staticmethod
    def from_dict(obj: Dict) -> Accounts:
        _dev_application = Account.from_dict(obj.get("dev_application"))
        _exploration = Account.from_dict(obj.get("exploration"))
        _prod = Account.from_dict(obj.get("prod"))
        _shared_services = Account.from_dict(obj.get("shared_services"))
        _staging = Account.from_dict(obj.get("staging"))
        return Accounts(_dev_application, _exploration, _prod, _shared_services, _staging)

    def get_account_by_id(self, account_id: str) -> Account:
        """
        :param account_id: AWS account id
        :return: Account object belonging to the AWS account id
        """
        for account in [
            self.dev_application,
            self.exploration,
            self.prod,
            self.shared_services,
            self.staging,
        ]:
            if account.account_id == account_id:
                return account


@dataclass(frozen=True)
class Environment:
    """This dataclass will describe the environment as well as properties of
    other services that are needed to run this code.

    A caller would call the `load_from_metadata` method with the key that holds
    the env. variables, ie `/mlops/environment`.

    .. code-block:: python

    ENVIRONMENT = Environment.load_from_metadata(["/mlops/environment"])

    The data returned will be this dataclass.

    .. code-block:: python
    Environment(
        project_name='trap',
        accounts=Accounts(
            dev_application=Account(
                account_id='812532035491',
                env_prefix='None',
                account_name='None',
                sagemaker_kms_key_id='None'
            ),
            exploration=Account(
                account_id='294819884533',
                env_prefix='ns',
                account_name='wkl-ns-model-exploration',
                sagemaker_kms_key_id='ee45dec1-7f9e-4387-ab75-ce1a93cfad56'
            ),
            prod=Account(
                account_id='188875420175',
                env_prefix='t',
                account_name='wkl-t-model-execution',
                sagemaker_kms_key_id='2f0aeaa1-fcab-4bd2-ae1f-a6b8dfd60dde'
            ),
            shared_services=Account(
                account_id='239453240794',
                env_prefix='None',
                account_name='wkl-p-shared-services',
                sagemaker_kms_key_id='None'
            ),
            staging=Account(
                account_id='740837425924',
                env_prefix='d',
                account_name='wkl-d-model-execution',
                sagemaker_kms_key_id='f54bf540-d6d2-412a-8303-875d81bdb026'
            )
        ),
        glue_crawlers_inputs=GlueCrawlersInputs(
            glue_crawler_connection_name='glue-crawler-model-output-vpc-connection',
            model_output_database_name='model_outputs'
        ),
        has_sensitive_data=False,
        networking=Networking(
            subnet_ids=[
                'subnet-0471886a16d9566c8',
                'subnet-07444a3a1eb29bbc9',
                'subnet-0aa64443617367b51'
            ],
            vpc_endpoint_sg_id='sg-0ac2d4b583d33cc1a',
            vpc_id='vpc-01b2e6c19cb3f0ed5'
        )
    )
    """

    project_name: str
    accounts: Accounts
    glue_crawlers_inputs: GlueCrawlersInputs
    has_sensitive_data: bool
    networking: Networking

    @staticmethod
    def from_dict(obj: Dict) -> Environment:
        """

        :param obj: _description_
        :type obj: Dict
        :return: _description_
        :rtype: Environment
        """
        _accounts = Accounts.from_dict(obj.get("accounts"))
        _project_name = str(obj.get("project_name"))
        _glue_crawlers_inputs = GlueCrawlersInputs.from_dict(obj.get("glue_crawlers_inputs"))
        _has_sensitive_data = bool(obj.get("has_sensitive_data"))
        _networking = Networking.from_dict(obj.get("networking"))
        return Environment(
            _project_name,
            _accounts,
            _glue_crawlers_inputs,
            _has_sensitive_data,
            _networking,
        )

    @staticmethod
    def load_from_metadata(key: str, parameters_driver: Parameters = None) -> Environment:
        """Load environment values from a key.

        :param parameters_driver: An object that implements a metadata
            storage driver that can retrieve the metadata
        :type parameters: Parameters
        :param key: Key to retrieve
        :type key: str
        :return: Environment object created from the loaded json
        """
        p = Parameters() if parameters_driver is None else parameters_driver
        env = p.get_parameters(keys=[key])
        jsonstring = json.loads(env[key])
        return Environment.from_dict(jsonstring)

    @staticmethod
    def load(parameters_driver: Parameters = None) -> Environment:
        """Load environment values from the key "/mlops/environment".

        :param parameters_drive: An object that implements a metadata
            storage
        :type parameters: Parameters
        :return: Environment object created from the loaded json
        """
        return Environment.load_from_metadata(parameters_driver=parameters_driver, key="/mlops/environment")
