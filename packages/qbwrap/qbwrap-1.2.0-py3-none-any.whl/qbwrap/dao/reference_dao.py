#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from ..dto.reference_dto import ReferenceDTO


class ReferenceDAO:
    """! Reference DAO."""

    # CONSIDER: This was initially added as a singleton.
    #  Right now it is actually used once but might come handy in future.
    #  By design it makes sense for it to be a singleton but maybe remove it
    #  in the future as "code cleanup".

    __reference_dao_instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__reference_dao_instance:
            cls.__reference_dao_instance = super().__new__(cls)

        return cls.__reference_dao_instance

    def __init__(self):
        self.__references = {}

    def get_reference(self, reference_path: str) -> ReferenceDTO:
        """! Reference getter."""

        return self.__references[reference_path]

    def add_reference(self, reference: ReferenceDTO):
        """! Reference getter."""

        reference_path = reference.get_path()
        self.__references[reference_path] = reference
