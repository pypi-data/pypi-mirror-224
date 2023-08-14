#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from dataclasses import dataclass
from subprocess import run
from typing import List

from ..dto.run_action_options_dto import RunActionOptionsDTO
from ..util.user_util import UserUtil


@dataclass
class RunAction:
    """! Run action."""

    __command_arguments: List[str]
    __options: RunActionOptionsDTO

    def execute(self):
        """! Execute the Run action."""

        arguments = []

        if UserUtil.user_is_unprivileged() and self.__options.get_become_root():
            if self.__options.get_become_method() == "su":
                su_subcommand = " ".join(
                    [f'"{s}"' for s in self.__command_arguments]
                )

                arguments.append("su")
                arguments.append("-c")
                arguments.append(su_subcommand)
            else:
                arguments.append(self.__options.get_become_method())
                arguments.extend(self.__command_arguments)
        else:
            arguments.extend(self.__command_arguments)

        # Show what will be executed.
        if not self.__options.get_quiet_execution():
            print(" * Executing: ", end="")

            for argument in arguments:
                print(argument, end=" ")

            print("")

        if not self.__options.get_fake_execution():
            run(arguments, check=True)
