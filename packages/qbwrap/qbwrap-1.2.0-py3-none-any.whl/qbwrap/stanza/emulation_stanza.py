#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from typing import Literal
from typing import Union

from ..dto.field_dto import FieldDTO
from .base_stanza import BaseStanza


class EmulationStanza(BaseStanza):
    """! Emulation stanza"""

    def __init__(self):
        super().__init__(stanza_name="emulation")

        self.get_fields_dao().add_field(FieldDTO("use", bool))
        self.get_fields_dao().add_field(FieldDTO("type", str))
        self.get_fields_dao().add_field(FieldDTO("arch", str))

        self.bind_fields()

    def get_use(self) -> bool:
        """! Return emulation.use."""

        return self.get_field_data("use")

    def get_type(self) -> Union[str, Literal[False]]:
        """! Return emulation.type."""

        emulation_type = self.get_field_data("type")

        if emulation_type == "none":
            return False

        return emulation_type

    def get_arch(self) -> Union[str, Literal[False]]:
        """! Return emulation.arch."""

        emulation_arch = self.get_field_data("arch")

        if emulation_arch == "native":
            return False

        return emulation_arch
