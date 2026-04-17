import argparse
import importlib
import os
import pkgutil
import sys
from argparse import ArgumentParser
from typing import Any


# Dynamically load all command modules and subcommands
def load_subcommands(subparsers, package_name):
    package = importlib.import_module(package_name)
    package_dir = os.path.dirname(package.__file__)

    for _, module_name, is_pkg in pkgutil.iter_modules([package_dir]):
        if is_pkg:
            # Recursively load subcommands
            load_subcommands(subparsers, f"{package_name}.{module_name}")
        else:
            module = importlib.import_module(f"{package_name}.{module_name}")
            if hasattr(module, 'setup_parser'):
                module.setup_parser(subparsers)


def verify_and_print_subcommand_help(subcommands: list[str],
                                     commands: list[Any],
                                     parsers: list[ArgumentParser],
                                     args):
    for subcommand, command, parser in zip(subcommands, commands, parsers):
        if args.subcommand == subcommand and command is None:
            parser.print_help()
            sys.exit(0)


def main():
    parser = argparse.ArgumentParser(prog="arcs",
                                     description="AR-Corp-Solutions command-line interface for managing various operations. "
                                                 "This CLI provides dynamically loaded subcommands for efficient execution of tasks across these domains. "
                                                 "Run with the '-v' or '--version' flag to display the current version of the CLI.")
    parser.add_argument('-v', '--version',
                        action="store_true",
                        help="Display cli version")
    subparsers = parser.add_subparsers(dest="subcommand")

    # Load TOTP subcommands
    totp_parser = subparsers.add_parser('totp', help="TOTP related commands")
    github_subparsers = totp_parser.add_subparsers(dest="totp_command")
    load_subcommands(github_subparsers, 'argparser.totp')

    # Load Webserver subcommands
    webserver_parser = subparsers.add_parser('webserver', help="Webserver related commands")
    webserver_subparsers = webserver_parser.add_subparsers(dest="webserver_command")
    load_subcommands(webserver_subparsers, 'argparser.webserver')

    args = parser.parse_args()

    verify_and_print_subcommand_help(subcommands=['totp',
                                                  'webserver'],
                                     commands=[args.totp_command if 'totp_command' in args else None,
                                               args.webserver_command if 'webserver_command' in args else None],
                                     parsers=[totp_parser,
                                              webserver_parser],
                                     args=args)

    # Call the corresponding function if available
    if hasattr(args, 'func'):
        args.func(args)
    elif args.version:
        import ast

        with open("setup.py", "r") as f:
            tree = ast.parse(f.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.keyword) and node.arg == "version":
                print(f"sentinel-authenticator version: {node.value.s}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
