#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from typing import List

from ..dto.bind_dto import BindDTO
from ..dto.field_dto import FieldDTO
from ..dto.tmpfs_device_dto import TmpfsDeviceDTO

from ..util.bind_util import BindUtil
from ..util.device_util import DeviceUtil
from ..util.list_util import ListUtil

from .base_stanza import BaseStanza


class MountStanza(BaseStanza):
    """! Mount stanza"""

    def __init__(self):
        super().__init__(stanza_name="mount")

        self.get_fields_dao().add_field(FieldDTO("rw", list))
        self.get_fields_dao().add_field(FieldDTO("ro", list))
        self.get_fields_dao().add_field(FieldDTO("dev", list))
        self.get_fields_dao().add_field(FieldDTO("proc", list))
        self.get_fields_dao().add_field(FieldDTO("tmpfs", list))

        self.bind_fields()

    def __get_bind(self, bind_name: str) -> List[BindDTO]:
        bind_listing = self.get_field_data(bind_name)

        if not bind_listing:
            return []

        bind_pairs_list = ListUtil.make_pairs_list(bind_listing)

        return [BindUtil.make_bind(pair) for pair in bind_pairs_list]

    def get_rw(self) -> List[BindDTO]:
        """! Return mount.rw."""

        return self.__get_bind("rw")

    def get_ro(self) -> List[BindDTO]:
        """! Return mount.ro."""

        return self.__get_bind("ro")

    def __get_tmpfs_device(self) -> List[TmpfsDeviceDTO]:
        special_device_listing = self.get_field_data("tmpfs")

        if not special_device_listing:
            return []

        return [DeviceUtil.make_tmpfs_device(data) for data in special_device_listing]

    def get_dev(self) -> List[str]:
        """! Return mount.dev."""

        return self.get_field_data("dev") or []

    def get_proc(self) -> List[str]:
        """! Return mount.proc."""

        return self.get_field_data("proc") or []

    def get_tmpfs(self) -> List[TmpfsDeviceDTO]:
        """! Return mount.tmpfs."""

        return self.__get_tmpfs_device()
