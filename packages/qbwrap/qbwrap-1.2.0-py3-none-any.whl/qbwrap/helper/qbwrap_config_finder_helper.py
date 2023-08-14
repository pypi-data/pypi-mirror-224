#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from os import path

from typing import Union

from .qbwrap_config_collection_helper import QBwrapConfigCollectionHelper
from .qbwrap_config_file_helper import QBwrapConfigFileHelper


class QBwrapConfigFinderHelper:
    """! QBwrap config file helper."""

    def __init__(
            self,
            use_collection_always: bool,
            use_collection_never: bool,
            override_collection_path: Union[str, None],
            quiet_execution: bool,
    ):
        self.__override_collection_path = override_collection_path
        self.__quiet_execution = quiet_execution
        self.__use_collection_always = use_collection_always
        self.__use_collection_never = use_collection_never

        self.__config_file = None

    def find_config_file(self, config_name):
        """! Setup config file by finding first available config_name."""

        if path.exists(config_name) and not self.__use_collection_always:
            qbwrap_config_file_path = config_name
        elif self.__use_collection_never:
            raise RuntimeError("main: specified QBwrap config file was not found")
        else:
            qbwrap_collection = QBwrapConfigCollectionHelper()

            # Ensure only initial collection (in ".config").
            qbwrap_collection.ensure_collection()

            if collection_path := self.__override_collection_path:
                if not self.__quiet_execution:
                    print(f' * Setting QBwrap collection to "{collection_path}"')

                qbwrap_collection.set_collection_path(collection_path)

            qbwrap_config_file_path = qbwrap_collection.get_config_path(config_name)

        if not self.__quiet_execution:
            print(f' * Using QBwrap file "{qbwrap_config_file_path}"')

        self.__config_file = QBwrapConfigFileHelper(qbwrap_config_file_path)

    def get_config(self):
        """! Get config data."""

        if self.__config_file is not None:
            self.__config_file.load_config()

            config = self.__config_file.get_config()

            return config

        raise RuntimeError("get_config: config file was not initialized")
