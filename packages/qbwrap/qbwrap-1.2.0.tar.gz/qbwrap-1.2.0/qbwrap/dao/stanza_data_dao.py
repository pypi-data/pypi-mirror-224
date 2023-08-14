#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from typing import Any
from typing import Dict


class StanzaDataDAO:
    """! Stanza data DAO."""

    def __init__(self):
        self.__data: Dict[str, Any] = {}

    def get_data(self, data_name: str) -> Any:
        """!
        Get a stanza data value.
        """

        return self.__data[data_name]

    def set_data(self, data_name: str, data_content: Any):
        """!
        Add a stanza data value.
        """

        self.__data[data_name] = data_content
