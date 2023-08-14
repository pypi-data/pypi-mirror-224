#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from dataclasses import dataclass


@dataclass
class BindDTO:
    """! Bind DTO."""

    __real_location: str
    __sandbox_location: str

    def get_real_location(self) -> str:
        """! Bind DTO real_location getter."""

        return self.__real_location

    def set_real_location(self, real_location: str):
        """! Bind DTO real_location setter."""

        self.__real_location = real_location

    def get_sandbox_location(self) -> str:
        """! Bind DTO sandbox_location getter."""

        return self.__sandbox_location

    def set_sandbox_location(self, sandbox_location: str):
        """! Bind DTO sandbox_location getter."""

        self.__sandbox_location = sandbox_location
