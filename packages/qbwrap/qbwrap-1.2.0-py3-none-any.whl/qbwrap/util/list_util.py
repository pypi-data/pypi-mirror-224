#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from typing import Any
from typing import List


class ListUtil:
    """! List util."""

    @staticmethod
    def make_pair(any_object: Any) -> List[Any]:
        """!
        Duplicate given object into a list.

        @param any_object: object to duplicate
        @return list of duplicate object
        """

        return [any_object, any_object]

    @classmethod
    def single_to_pair(cls, any_object: Any) -> List[Any]:
        """!
        Duplicate given object if it is not a list, otherwise return it.

        @param any_object: object of any type
        @return list
        """

        if isinstance(any_object, list):
            return any_object

        return cls.make_pair(any_object)

    @classmethod
    def make_pairs_list(cls, any_objects: List[Any]) -> List[List[Any]]:
        """!
        Call single_to_pair on a given list.

        @param any_object: list
        @return list of lists
        """

        return [cls.single_to_pair(any_object) for any_object in any_objects]
