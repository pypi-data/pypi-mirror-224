#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from typing import List

from ..dto.bind_dto import BindDTO


class BindUtil:
    """! Bind util."""

    @staticmethod
    def make_bind(properties_list: List[str]) -> BindDTO:
        """! Return a BindDTO from a given list."""

        real_location = properties_list[0]
        sandbox_location = properties_list[1]

        return BindDTO(real_location, sandbox_location)
