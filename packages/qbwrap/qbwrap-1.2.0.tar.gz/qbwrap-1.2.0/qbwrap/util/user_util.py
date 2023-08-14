#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from os import geteuid


class UserUtil:
    """! User util."""

    @staticmethod
    def user_is_privileged() -> bool:
        """!
        Check if the current user has root privileges.

        @return whether user is privileged
        """

        return geteuid() == 0

    @classmethod
    def user_is_unprivileged(cls) -> bool:
        """!
        Check if the current user does not have root privileges.

        @return whether user is unprivileged
        """

        return not cls.user_is_privileged()
