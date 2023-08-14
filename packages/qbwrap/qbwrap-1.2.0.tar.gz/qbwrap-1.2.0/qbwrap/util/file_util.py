#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from typing import Iterator


class FileUtil:
    """! File util."""

    @staticmethod
    def read_by_4kb(file_buffer) -> Iterator:
        """! Read by 4K bytes from a file_buffer."""

        return iter(lambda: file_buffer.read(4096), b"")
