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

from ..dto.field_dto import FieldDTO
from .base_stanza import BaseStanza


CoreStanzaLocation = Union[str, Literal[False]]
CoreStanzaHostname = Union[str, Literal[False]]


class CoreStanza(BaseStanza):
    """! Core stanza."""

    def __init__(self):
        super().__init__(stanza_name="core")

        self.get_fields_dao().add_field(FieldDTO("location", str))
        self.get_fields_dao().add_field(FieldDTO("hostname", str))
        self.get_fields_dao().add_field(FieldDTO("new_session", bool))
        self.get_fields_dao().add_field(FieldDTO("process", str))
        self.get_fields_dao().add_field(FieldDTO("env", list))

        self.bind_fields()

    def get_location(self) -> CoreStanzaLocation:
        """! Return core.location or raise a runtime error."""

        return self.get_field_data("location")

    def get_hostname(self) -> CoreStanzaHostname:
        """! Return core.hostname."""

        return self.get_field_data("hostname")

    def get_new_session(self) -> bool:
        """! Return core.new_session."""

        return self.get_field_data("new_session")

    def get_process(self) -> str:
        """! Return core.process or "sh"."""

        return self.get_field_data("process") or "sh"

    def get_env(self) -> List[List[str]]:
        """! Return core.process or "sh"."""

        return self.get_field_data("env") or []
