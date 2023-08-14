#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from typing import List
from typing import Literal
from typing import Union

from ..dto.reference_dto import ReferenceDTO

from ..stanza.core_stanza import CoreStanza
from ..stanza.emulation_stanza import EmulationStanza
from ..stanza.mount_stanza import MountStanza
from ..stanza.unshare_stanza import UnshareStanza
from ..stanza.user_stanza import UserStanza

from ..util.reference_util import ReferenceUtil
from ..util.size_util import SizeUtil

from .qbwrap_stanza_delegate_dao import QBwrapStanzaDelegateDAO
from .reference_dao import ReferenceDAO


SpecialDeviceSizeType = Union[str, Literal[False]]


class QBwrapOptionsDAO(QBwrapStanzaDelegateDAO):
    """! QBwrap options DAO."""

    def __init__(
        self,
        config,
        default_special_device_size: SpecialDeviceSizeType,
    ):
        super().__init__(config)

        self.__default_special_device_size = default_special_device_size

        self.__process = ""
        self.__reference_dao = ReferenceDAO()

    def get_process(self) -> str:
        """! Return command that shall be executed."""

        return self.__process

    def get_core_stanza_options(self) -> List[str]:
        """! Get options based on CoreStanza."""

        core_stanza = self._get_stanza(CoreStanza)
        options = []

        self.__reference_dao.add_reference(ReferenceDTO(
            "core.location",
            core_stanza.get_location(),
        ))

        if hostname := core_stanza.get_hostname():
            options.append("--unshare-uts")  # Required for setting hostname.
            options.append("--hostname")
            options.append(hostname)

        if core_stanza.get_new_session():
            options.append("--new-session")

        for env_setting in core_stanza.get_env():
            env_key = env_setting[0]
            env_value = env_setting[1]

            self.__reference_dao.add_reference(ReferenceDTO(
                f"core.env.{env_key}",
                env_value,
            ))

            options.append("--setenv")
            options.append(env_key)
            options.append(env_value)

        self.__process = core_stanza.get_process()

        return options

    def get_emulation_stanza_options(self) -> List[str]:
        """! Get options based on EmulationStanza."""

        emulation_stanza = self._get_stanza(EmulationStanza)
        options = []

        if emulation_stanza.get_use():
            emulator: Union[str, Literal[False]] = False

            if emulation_stanza.get_type() == "qemu":
                emulation_arch = emulation_stanza.get_arch()

                # Exception for amd64
                if emulation_arch == "amd64":
                    emulator = "qemu-x86_64"

                # Exception for arm64
                elif emulation_arch == "arm64":
                    emulator = "qemu-aarch64"

                else:
                    emulator = f"qemu-{emulation_arch}"

            if emulator:
                options = [emulator]

        return options

    def get_unshare_stanza_options(self) -> List[str]:
        """! Get options based on UnshareStanza."""

        unshare_stanza = self._get_stanza(UnshareStanza)
        options = []

        for field_name in unshare_stanza.get_fields_dao().get_field_names():
            if unshare_stanza.is_unshared(field_name):
                canonic_name = field_name.replace("_", "-")
                option_name = f"--unshare-{canonic_name}"

                options.append(option_name)

        return options

    def get_user_stanza_options(self) -> List[str]:
        """! Get options based on UserStanza."""

        user_stanza = self._get_stanza(UserStanza)
        options = []

        if group_identifier := user_stanza.get_user_identifier():
            options.append("--gid")
            options.append(group_identifier)

        if user_identifier := user_stanza.get_user_identifier():
            options.append("--uid")
            options.append(user_identifier)

        return options

    def __special_device_options(self, device, device_type: str) -> List[str]:
        # Here "device" is a actually only a device mount point string.

        return [f"--{device_type}", device]

    def __tmpfs_device_options(self, device) -> List[str]:
        options = []
        device_options = device.get_options()

        size: Union[str, Literal[False]] = False

        if device_size := device_options.get_size():
            size = SizeUtil.size_bytes(device_size)
        elif device_size := self.__default_special_device_size:
            size = SizeUtil.size_bytes(device_size)

        if size:
            options.append("--size")
            options.append(size)

        if device_perms := device_options.get_perms():
            options.append("--perms")
            options.append(f"{device_perms}")

        options.append("--tmpfs")
        options.append(device.get_mountpoint())

        return options

    def __dereference(self, maybe_reference: str) -> str:
        if ReferenceUtil.is_reference_string(maybe_reference):
            reference = self.__reference_dao.get_reference(
                ReferenceUtil.reference_string_to_path(maybe_reference)
            )
            value = reference.get_value()
        else:
            value = maybe_reference

        return value

    def __normal_device_options(self, bind, bind_type: str):
        return [
            f"--{bind_type}",
            self.__dereference(bind.get_real_location()),
            self.__dereference(bind.get_sandbox_location()),
        ]

    def get_mount_stanza_options(self) -> List[str]:
        """! Get options based on MountStanza."""

        mount_stanza = self._get_stanza(MountStanza)
        options = []

        for bind in mount_stanza.get_rw():
            options.extend(self.__normal_device_options(bind, "bind"))

        for bind in mount_stanza.get_ro():
            options.extend(self.__normal_device_options(bind, "ro-bind"))

        for device in mount_stanza.get_dev():
            options.extend(self.__special_device_options(device, "dev"))

        for device in mount_stanza.get_proc():
            options.extend(self.__special_device_options(device, "proc"))

        for device in mount_stanza.get_tmpfs():
            options.extend(self.__tmpfs_device_options(device))

        return options
