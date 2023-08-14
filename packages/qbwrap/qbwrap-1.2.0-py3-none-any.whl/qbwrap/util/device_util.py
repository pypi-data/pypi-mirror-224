#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from ..dto.tmpfs_device_dto import TmpfsDeviceDTO
from ..dto.tmpfs_device_options_dto import TmpfsDeviceOptionsDTO


class DeviceUtil:
    """! Device util."""

    @staticmethod
    def make_tmpfs_device(properties_list: list) -> TmpfsDeviceDTO:
        """! Create a DeviceDTO object from a list."""

        tmpfs_device_name = properties_list[0]
        tmpfs_device_dict = properties_list[1]

        tmpfs_device_options = TmpfsDeviceOptionsDTO()

        if "size" in tmpfs_device_dict:
            tmpfs_device_options.set_size(tmpfs_device_dict["size"])

        if "perms" in tmpfs_device_dict:
            tmpfs_device_options.set_perms(tmpfs_device_dict["perms"])

        return TmpfsDeviceDTO(tmpfs_device_name, tmpfs_device_options)
