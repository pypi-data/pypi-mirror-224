import logging
from json import (
    dumps,
    loads,
)
from pathlib import Path
from sys import exit
from typing import Optional

import botocore
import click
import yaml

from mlopscfg.parameters import Parameters

from . import __version__


def get_parameter_store():
    return Parameters()


@click.group()
@click.version_option(__version__)
@click.option("--debug", prompt=False, is_flag=True)
def cli(debug):
    if debug:
        log.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        log.addHandler(handler)

        log.debug("debug logging on")
    pass


##
# Get command


@cli.command(no_args_is_help=True)
@click.option("--key", required=True, help="Key to get from Backend")
def get(key: str) -> None:
    """Retrieves the value of a key from the Backend.

    Returns the raw value.
    """
    parameters = get_parameter_store().get_parameters(keys=[key])
    print(parameters[key])


##
# Tree command


@cli.command(no_args_is_help=True)
@click.option("--path", required=True, help="Path to traverse to get all values from")
def tree(path: str) -> None:
    """Retrieves all the keys and values under certain path.

    For naming restrictions look at
    :py: func:SSMParameterStore.put_parameter
    """
    parameters = get_parameter_store().get_parameters_by_path(base_path=path, recursive=True, nested=False)
    tmp = {}
    for k, v in parameters.items():
        tmp[k] = loads(v)
    print(dumps(tmp, indent=4))


##
# Put command


@cli.command(no_args_is_help=True)
@click.option(
    "--overwrite/--no-overwrite",
    default=False,
    prompt=False,
    help="Overwrite the value if it already exists. Default False",
)
@click.option("--value", default=None, help="A string to be stored in the Backend, limit of 4kb")
@click.option("--path", help="The name of the key where it will be stored")
@click.argument("file", type=click.Path(exists=True), required=False)
@click.option(
    "--to-json",
    is_flag=True,
    default=False,
    prompt=False,
    help="Enables converting a YAML file to JSON, limit of 4kb",
)
@click.option(
    "--yaml-node-path",
    default=None,
    help="The PATH to the top level node in the YAML that will be stored, separated by '/' , ie projects/test",
)
def put(
    value: str,
    path: str,
    to_json: bool,
    yaml_node_path: str = None,
    overwrite: bool = False,
    file: Optional[str] = None,
) -> str:
    """Stores a string value in a Backend path.

    Supports reading from a yaml file , convert it to json and store the result.
    If a yaml node is specified then only the content of that node will be stored.

    FILE: (optional) Path to the file to be used as source of the value
    """
    if not file and not value:
        logging.fatal("Either a value or a file must be specified, exiting")
        exit(-2)

    final_value = value
    if file:
        logging.debug(f"Reading from file: {file}")
        final_value = Path(file).read_text()
        # Convert YAML to dictionary and store a node
        if yaml_node_path:
            try:
                dict_value = yaml.safe_load(final_value)
                dict_path = yaml_node_path.split("/")
                final_value = deref_multi(dict_value, dict_path)
            except KeyError as e:
                logging.fatal(f"Yaml node {e} not found, exiting")
                exit(-1)
        if to_json:
            final_value = dumps(final_value)

    try:
        ret = get_parameter_store().put_parameter(path=path, value=final_value, overwrite=overwrite)
        print(f"{ret}")
    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "ParameterAlreadyExists":
            logging.fatal("The path used already exists as key in the Backend, exiting")
        else:
            logging.fatal(f"Error returned: {e}")
        exit(-3)


cli.add_command(get)
cli.add_command(put)
cli.add_command(tree)


def deref_multi(data, keys):
    return deref_multi(data[keys[0]], keys[1:]) if keys else data


if __name__ == "__main__":
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    cli()
