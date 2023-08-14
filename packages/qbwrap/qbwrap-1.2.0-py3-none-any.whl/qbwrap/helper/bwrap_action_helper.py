#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from typing import List

from ..action.run_action import RunAction


class BwrapActionHelper:
    """! Bwrap action helper."""

    def __init__(self):
        self.__bwrap_executable = "bwrap"
        self.__bwrap_arguments = []
        self.__run_action = False

    def set_bwrap_executable(self, bwrap_executable: str):
        """! Bwrap action helper bwrap_executable setter."""

        self.__bwrap_executable = bwrap_executable

    def extend(self, command_arguments_list: List[str]):
        """! Extend the bwrap_arguments."""

        self.__bwrap_arguments.extend(command_arguments_list)

    def setup_process(self, process: str):
        """! Setup for process spawned by bwrap."""

        # Setup for the process to execute.
        # Mostly because of shell + "run" quoting issue... but also "PATH"?
        self.__bwrap_arguments.append("/bin/sh")
        self.__bwrap_arguments.append("-c")

        self.__bwrap_arguments.append(process)

    def __get_command_arguments(self) -> List[str]:
        return [self.__bwrap_executable] + self.__bwrap_arguments

    def setup_run_action(self, *args, **kwargs):
        """!
        Setup for run action.

        This method takes all of RunAction class arguments except
        command_arguments.
        For more information see the RunAction initializer.
        """

        self.__run_action = RunAction(
            self.__get_command_arguments(),
            *args,
            **kwargs,
        )

    def get_run_action(self) -> RunAction:
        """! Bwrap action helper run_action getter."""

        return self.__run_action
