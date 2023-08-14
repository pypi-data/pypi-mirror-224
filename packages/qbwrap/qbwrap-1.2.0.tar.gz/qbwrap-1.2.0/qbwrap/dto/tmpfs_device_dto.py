#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from dataclasses import dataclass

from .tmpfs_device_options_dto import TmpfsDeviceOptionsDTO


@dataclass
class TmpfsDeviceDTO:
    """! Device DTO."""

    __mountpoint: str
    __options: TmpfsDeviceOptionsDTO

    def get_mountpoint(self) -> str:
        """! Device DTO mountpoint getter."""

        return self.__mountpoint

    def set_mountpoint(self, mountpoint: str):
        """! Device DTO mountpoint setter."""

        self.__mountpoint = mountpoint

    def get_options(self) -> TmpfsDeviceOptionsDTO:
        """! Device DTO options getter."""

        return self.__options

    def set_options(self, options: TmpfsDeviceOptionsDTO):
        """! Device DTO options setter."""

        self.__options = options
