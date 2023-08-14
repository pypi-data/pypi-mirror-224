#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from ..dto.field_dto import FieldDTO
from .base_stanza import BaseStanza


class SetupStanza(BaseStanza):
    """! Setup stanza"""

    def __init__(self):
        super().__init__(stanza_name="setup")

        self.get_fields_dao().add_field(FieldDTO("url", str))
        self.get_fields_dao().add_field(FieldDTO("sha", str))
        self.get_fields_dao().add_field(FieldDTO("privileged", bool))

        self.bind_fields()

    def __get_url_archive(self) -> str:
        """! Return basename of setup.url."""

        return self.get_field_data("url").split("/")[-1]

    def is_setup_available(self) -> bool:
        """! Return whether setup stanza is configured."""

        # Check only the fields that are required.
        # In this case "url" and "sha" are strictly necessary.
        is_setup_url = bool(self.get_field_data("url"))
        is_setup_sha = bool(self.get_field_data("sha"))

        return is_setup_url and is_setup_sha

    def get_url(self) -> str:
        """! Return setup.location or raise a runtime error."""

        setup_url = self.get_field_data("url")

        if not setup_url:
            raise RuntimeError("get_url: URL for SetupStanza not provided")

        return self.get_field_data("url")

    def get_archive(self) -> str:
        """! Return setup.archive or raise a runtime error."""

        try:
            return self.__get_url_archive()
        except Exception as exception:
            raise RuntimeError(
                "get_name: could not get target archive name"
            ) from exception

    def get_sha(self) -> str:
        """! Return setup.sha or raise a runtime error."""

        setup_sha = self.get_field_data("sha")

        if not setup_sha:
            raise RuntimeError("get_sha: SHA for SetupStanza not provided")

        return setup_sha

    def get_privileged(self) -> bool:
        """! Return setup.privileged."""

        setup_privileged = self.get_field_data("privileged")

        # Default is "True".
        if not setup_privileged:
            return True

        return setup_privileged
