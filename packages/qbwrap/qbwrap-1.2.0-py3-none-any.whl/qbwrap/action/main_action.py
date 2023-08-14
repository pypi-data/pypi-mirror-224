#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from codecs import decode

import tomli

from .. import __description__
from .. import __version__

from ..action.setup_action import SetupAction

from ..dao.argument_parser_dao import ArgumentParserDAO
from ..dao.qbwrap_options_dao import QBwrapOptionsDAO
from ..dao.qbwrap_setup_dao import QBwrapSetupDAO

from ..dto.run_action_options_dto import RunActionOptionsDTO

from ..helper.bwrap_action_helper import BwrapActionHelper
from ..helper.qbwrap_config_finder_helper import QBwrapConfigFinderHelper


class MainAction:
    """! Main action."""

    def __init__(self):
        self.__verbose = False
        self.__argument_parser = ArgumentParserDAO(__description__, __version__)

    def __argument_to_tomli(self, argument_string):
        return tomli.loads(decode(argument_string, "unicode_escape"))

    def __get_config(self):
        use_collection_always = self.__argument_parser.get_use_collection_always()
        use_collection_never = self.__argument_parser.get_use_collection_never()

        if self.__verbose and use_collection_always:
            print(" * Will not use any QBwrap files in current directory...")

        if self.__verbose and use_collection_never:
            print(" * Will not use QBwrap collection...")

        qbwrap_config_finder_helper = QBwrapConfigFinderHelper(
            use_collection_always=use_collection_always,
            use_collection_never=use_collection_never,
            override_collection_path=self.__argument_parser.get_collection_path(),
            quiet_execution=(not self.__verbose),
        )
        arg_file = self.__argument_parser.get_file()

        qbwrap_config_finder_helper.find_config_file(arg_file)

        qbwrap_config = qbwrap_config_finder_helper.get_config()

        return qbwrap_config

    def __setup(self, qbwrap_config):
        force_setup = self.__argument_parser.get_force_setup()
        qbwrap_setup = QBwrapSetupDAO(qbwrap_config)

        qbwrap_setup.setup_location()

        if force_setup or not qbwrap_setup.location_exists():
            qbwrap_setup.setup_stanza()

            if not qbwrap_setup.get_setup_stanza().is_setup_available():
                print(" * Setup might be necessary but is not configured.")

            setup_action = SetupAction(
                argument_parser=self.__argument_parser,
                qbwrap_setup_dao=qbwrap_setup,
            )

            setup_action.execute()

    def execute(self):
        """! Execute the Setup action."""

        self.__argument_parser.parse()

        self.__verbose = not self.__argument_parser.get_quiet()

        qbwrap_config = self.__get_config()

        if merge := self.__argument_parser.get_merge():
            qbwrap_config = qbwrap_config | self.__argument_to_tomli(merge)

        qbwrap_options = QBwrapOptionsDAO(
            qbwrap_config,
            self.__argument_parser.get_default_special_device_size(),
        )

        if not self.__argument_parser.get_no_setup():
            self.__setup(qbwrap_config)

        bwrap_action_helper = BwrapActionHelper()

        bwrap_action_helper.extend(qbwrap_options.get_core_stanza_options())
        bwrap_action_helper.extend(qbwrap_options.get_unshare_stanza_options())
        bwrap_action_helper.extend(qbwrap_options.get_user_stanza_options())
        bwrap_action_helper.extend(qbwrap_options.get_mount_stanza_options())
        bwrap_action_helper.extend(qbwrap_options.get_emulation_stanza_options())

        # Override process.
        if process := self.__argument_parser.get_process():
            bwrap_action_helper.setup_process(process)
        else:
            bwrap_action_helper.setup_process(qbwrap_options.get_process())

        # Override bwrap executable.
        if bwrap_executable := self.__argument_parser.get_executable():
            bwrap_action_helper.set_bwrap_executable(bwrap_executable)

        bwrap_run_action_options = RunActionOptionsDTO(
            self.__argument_parser.get_become_root(),
            self.__argument_parser.get_become_root_method(),
            self.__argument_parser.get_fake(),
            self.__argument_parser.get_quiet(),
        )

        bwrap_action_helper.setup_run_action(bwrap_run_action_options)

        if self.__verbose:
            print(" * Entering the bubblewrap chroot...")

        # And finally run bwrap.
        bwrap_run_action = bwrap_action_helper.get_run_action()
        bwrap_run_action.execute()
