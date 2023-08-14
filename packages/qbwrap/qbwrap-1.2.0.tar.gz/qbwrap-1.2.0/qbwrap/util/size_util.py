#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


class SizeUtil:
    """! Size util."""

    __size_multipliers = {
        "G": 1024 * 1024 * 1024,
        "M": 1024 * 1024,
        "K": 1024,
    }

    @classmethod
    def size_bytes(cls, size_string: str) -> str:
        """!
        Convert a size string with units to bytes.

        Examples:
          - "1" -> "1"
          - "5 G" -> "5368709120"

        @param size_string: string in special syntax
        @return bytes
        """

        try:
            size_pair = size_string.split(" ")
            size_number = float(size_pair[0])

            # "1" -> 1 B
            if len(size_pair) == 1:
                return f"{size_number}"

            size_unit = size_pair[1]
            size_multiplier = cls.__size_multipliers[size_unit]
            size_bytes_number = int(size_multiplier * size_number)

            # int -> str
            return f"{size_bytes_number}"

        except Exception as exception:
            raise RuntimeError(
                f'size_bytes: failed to parse size_string, given: "{size_string}"'
            ) from exception
