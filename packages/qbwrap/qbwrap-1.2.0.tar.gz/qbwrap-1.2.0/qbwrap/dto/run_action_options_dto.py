#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from dataclasses import dataclass


@dataclass
class RunActionOptionsDTO:
    """! Run action options DTO."""

    __become_root: bool
    __become_method: str
    __fake_execution: bool
    __quiet_execution: bool

    def get_become_root(self) -> bool:
        """! Run action options DTO become_root getter."""

        return self.__become_root

    def set_become_root(self, become_root):
        """! Run action options DTO become_root setter."""

        self.__become_root = become_root

    def get_become_method(self) -> str:
        """! Run action options DTO become_method getter."""

        return self.__become_method

    def set_become_method(self, become_method):
        """! Run action options DTO become_method setter."""

        self.__become_method = become_method

    def get_fake_execution(self) -> bool:
        """! Run action options DTO fake_execution getter."""

        return self.__fake_execution

    def set_fake_execution(self, fake_execution):
        """! Run action options DTO fake_execution setter."""

        self.__fake_execution = fake_execution

    def get_quiet_execution(self) -> bool:
        """! Run action options DTO quiet_execution getter."""

        return self.__quiet_execution

    def set_quiet_execution(self, quiet_execution):
        """! Run action options DTO quiet_execution setter."""

        self.__quiet_execution = quiet_execution
