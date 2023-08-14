#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from os import makedirs
from os import path


class QBwrapConfigCollectionHelper:
    """! QBwrap config collection helper."""

    def __init__(self):
        self.__collection_path = "~/.config/qbwrap/collection"

    def set_collection_path(self, collection_path: str):
        """! Set QBwrap collection path."""

        self.__collection_path = collection_path

    def __get_expanded_collection_path(self) -> str:
        return path.expanduser(self.__collection_path)

    def ensure_collection(self):
        """! Ensure the collection directory exists."""

        collection_path = self.__get_expanded_collection_path()

        if not path.exists(collection_path):
            makedirs(collection_path)

    def __check_collection(self):
        """! Check if the QBwrap collection exists."""

        collection_path = self.__get_expanded_collection_path()

        if not path.exists(collection_path):
            raise RuntimeError(
                "__check_collection: QBwrap collection does not exist at path "
                + f'"{collection_path}"'
            )

    def __add_prefix(self, config_name: str) -> str:
        return path.join(self.__get_expanded_collection_path(), config_name)

    def get_config_path(self, config_name: str) -> str:
        """! Get config data."""

        self.__check_collection()

        for config_extension in ["", ".toml", ".QBwrap.toml"]:
            config_path = self.__add_prefix(config_name + config_extension)

            if path.exists(config_path):
                return config_path

        raise RuntimeError(
            f'get_config_path: config file with name "{config_name}" '
            + "was not found in the QBwrap collection"
        )
