#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

from dataclasses import dataclass


@dataclass
class ReferenceDTO:
    """! Reference DTO."""

    __path: str
    __value: str

    def get_path(self) -> str:
        """! Reference DTO path getter."""

        return self.__path

    def set_path(self, path: str):
        """! Reference DTO path setter."""

        self.__path = path

    def get_value(self) -> str:
        """! Reference DTO value getter."""

        return self.__value

    def set_value(self, value: str):
        """! Reference DTO value getter."""

        self.__value = value
