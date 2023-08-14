#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from os import path

from typing import List
from typing import Optional

from ..stanza.core_stanza import CoreStanza
from ..stanza.setup_stanza import SetupStanza

from ..util.sha_util import ShaUtil

from .qbwrap_stanza_delegate_dao import QBwrapStanzaDelegateDAO


class QBwrapSetupDAO(QBwrapStanzaDelegateDAO):
    """! QBwrap setup DAO."""

    def __init__(self, config):
        super().__init__(config)

        self.__location: Optional[str] = None
        self.__setup_stanza: Optional[SetupStanza] = None

    def setup_stanza(self):
        """! Setup this object SetupStanza."""

        self.__setup_stanza = self._get_stanza(SetupStanza)

    def setup_location(self):
        """! Setup location."""

        core_stanza = self._get_stanza(CoreStanza)

        self.__location = core_stanza.get_location()

    def get_location(self) -> str:
        """! Return location."""

        if not self.__location:
            # location may either be not set up or unspecified in configuration
            raise RuntimeError("get_setup_stanza: location was not defined")

        return self.__location

    def location_exists(self) -> bool:
        """! Return whether the required location exists."""

        return path.exists(self.get_location())

    def get_setup_stanza(self) -> SetupStanza:
        """! Return SetupStanza that was set up."""

        if not self.__setup_stanza:
            raise RuntimeError("get_setup_stanza: SetupStanza was not set up")

        return self.__setup_stanza

    def __get_archive_output_path(self) -> str:
        archive_output_path = path.join(
            self.get_location(),
            self.get_setup_stanza().get_archive(),
        )

        return archive_output_path

    def get_download_command(self) -> List[str]:
        """! Return URL download command with it's arguments."""

        url_download_command = [
            "wget",
            self.get_setup_stanza().get_url(),
            "--output-document",
            self.__get_archive_output_path(),
        ]

        return url_download_command

    def get_extraction_command(self) -> List[str]:
        """! Return archive extraction command with it's arguments."""

        # Just use "tar" for now.
        archive_extraction_command = [
            "tar",
            "xf",
            self.__get_archive_output_path(),
            "-C",
            self.get_location(),
        ]

        return archive_extraction_command

    def verify_archive(self):
        """! Verify archive at a defined location using sha256 algorithm."""

        sum_calculated = ShaUtil.file_sha256(self.__get_archive_output_path())
        sum_wanted = self.__setup_stanza.get_sha()

        if not sum_calculated == sum_wanted:
            raise RuntimeError(
                "verify_archive_sha256: sha256 sums are not equal, "
                + f'given: "{sum_calculated}" '
                + f'but required "{sum_wanted}"'
            )
