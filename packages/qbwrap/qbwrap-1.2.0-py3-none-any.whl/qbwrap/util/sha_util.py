#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from hashlib import sha256

from .file_util import FileUtil


class ShaUtil:
    """! Sha util."""

    @staticmethod
    def file_sha256(file_path: str) -> str:
        """! Return a file sha256 sum."""

        sha256_sum = sha256()

        with open(file_path, "rb") as opened_file:
            for block in FileUtil.read_by_4kb(opened_file):
                sha256_sum.update(block)

        return sha256_sum.hexdigest()
