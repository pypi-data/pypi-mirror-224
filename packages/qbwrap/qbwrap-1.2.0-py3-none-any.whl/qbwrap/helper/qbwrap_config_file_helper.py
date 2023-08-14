#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from os import path

import tomli


class QBwrapConfigFileHelper:
    """! QBwrap config file helper."""

    def __init__(self, config_path):
        self.__config_path = path.abspath(config_path)
        self.__config_data = None

    def load_config(self):
        """! Load a file from config_path."""

        if not path.exists(self.__config_path):
            raise RuntimeError(
                f'load_config: file "{self.__config_path}" does not exist'
            )

        try:
            with open(self.__config_path, "rb") as opened_file:
                self.__config_data = tomli.load(opened_file)

        except Exception as exception:
            raise RuntimeError(
                f'load_config: file "{self.__config_path}" could not be loaded'
            ) from exception

    def get_config(self):
        """! Get config data."""

        if self.__config_data is not None:
            return self.__config_data

        raise RuntimeError("get_config: config file data was not loaded")
