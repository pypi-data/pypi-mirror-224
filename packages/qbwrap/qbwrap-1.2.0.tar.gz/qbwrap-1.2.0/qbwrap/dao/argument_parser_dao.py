#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from argparse import ArgumentParser


class ArgumentParserDAO:
    """! Argument parser DAO for custom set of command line arguments."""

    __argument_parser_dao_instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__argument_parser_dao_instance:
            cls.__argument_parser_dao_instance = super().__new__(cls)

        return cls.__argument_parser_dao_instance

    def __init__(self, description, version):
        parser = ArgumentParser(
            prog="qbwrap",
            description=f"%(prog)s - {description}",
            epilog="""Copyright (c) 2023, Maciej Barć <xgqt@riseup.net>.
            Licensed under the Mozilla Public License, v. 2.0.""",
        )

        parser.add_argument(
            "-V",
            "--version",
            action="version",
            version=f"%(prog)s {version}",
        )
        parser.add_argument(
            "-q",
            "--quiet",
            action="store_true",
            help="be quiet, limit information output",
        )
        parser.add_argument(
            "-f",
            "--fake",
            action="store_true",
            help="do not actually call bwrap",
        )
        parser.add_argument(
            "-r",
            "--root",
            action="store_true",
            help="call bwrap as root",
        )
        parser.add_argument(
            "-R",
            "--root-method",
            type=str,
            default="su",
            help="which method to use to become root",
        )
        parser.add_argument(
            "-S",
            "--dev-size",
            type=str,
            default=False,
            help="default size for special devices, eg. tmpfs",
        )
        parser.add_argument(
            "-e",
            "--executable",
            type=str,
            help='bubblewrap executable to call, defaults to "bwrap"',
        )
        parser.add_argument(
            "-p",
            "--process",
            type=str,
            help="override process command to start inside bwrap chroot",
        )
        parser.add_argument(
            "-m",
            "--merge",
            type=str,
            help="override any stanza of given QBwrap config",
        )
        parser.add_argument(
            "-P",
            "--collection-path",
            type=str,
            help="overwrite path of the QBwrap collection",
        )
        parser.add_argument(
            "-c",
            "--use-collection",
            choices=["default", "always", "never"],
            help="whether and how to use the QBwrap collection",
        )
        parser.add_argument(
            "--no-setup",
            action="store_true",
            help="do not run setup (from the setup stanza) even if required",
        )
        parser.add_argument(
            "--force-setup",
            action="store_true",
            help="force to run setup defined in the setup stanza",
        )

        parser.add_argument(
            "qbwrap_file",
            type=str,
            help="path to the QBwrap config file",
        )

        self.__args = None
        self.__parser = parser

    def parse(self):
        """! Parse arguments."""

        self.__args = self.__parser.parse_args()

    def get_quiet(self):
        """! Return args.quiet."""

        return self.__args.quiet

    def get_fake(self):
        """! Return args.fake."""

        return self.__args.fake

    def get_become_root(self):
        """! Return args.root."""

        return self.__args.root

    def get_default_special_device_size(self):
        """! Return args.dev_size."""

        return self.__args.dev_size

    def get_become_root_method(self):
        """! Return args.root_method."""

        return self.__args.root_method

    def get_executable(self):
        """! Return args.executable."""

        return self.__args.executable

    def get_process(self):
        """! Return args.process."""

        return self.__args.process

    def get_merge(self):
        """! Return args.merge."""

        return self.__args.merge

    def get_no_setup(self):
        """! Return args.no_setup."""

        return self.__args.no_setup

    def get_collection_path(self):
        """! Return args.collection_path."""

        return self.__args.collection_path

    def get_use_collection_always(self):
        """! Return whether args.use_collection is "always"."""

        return self.__args.use_collection == "always"

    def get_use_collection_never(self):
        """! Return whether args.use_collection is "never"."""

        return self.__args.use_collection == "never"

    def get_force_setup(self):
        """! Return args.force_setup."""

        return self.__args.force_setup

    def get_file(self):
        """! Return args.file."""

        return self.__args.qbwrap_file
