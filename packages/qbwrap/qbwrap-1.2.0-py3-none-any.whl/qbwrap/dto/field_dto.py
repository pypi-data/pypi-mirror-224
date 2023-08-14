#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from dataclasses import dataclass


@dataclass
class FieldDTO:
    """! Field DTO."""

    __name: str
    __type: str

    def get_name(self) -> str:
        """! Field DTO name getter."""

        return self.__name

    def set_name(self, name: str):
        """! Field DTO name setter."""

        self.__name = name

    def get_type(self):
        """! Field DTO type getter."""

        return self.__type

    def set_type(self, type):
        """! Field DTO type setter."""

        self.__type = type
