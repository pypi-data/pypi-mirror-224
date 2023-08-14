#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from ..action.main_action import MainAction


def main():
    """! Main."""

    main_action = MainAction()

    main_action.execute()


if __name__ == "__main__":
    main()
