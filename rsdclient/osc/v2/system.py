#   Copyright 2019 Intel, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

import json

from rsdclient.common import command


class ListSystem(command.Command):
    """List all systems."""

    _description = "List all Systems"

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        system_list = rsd_client.system.list()
        print(system_list)


class ShowSystem(command.Command):
    """Show system details."""

    _description = "Display system details"

    def get_parser(self, prog_name):
        parser = super(ShowSystem, self).get_parser(prog_name)
        parser.add_argument(
            'system',
            metavar='<system>',
            help='ID of the system.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        system_detail = rsd_client.system.show(parsed_args.system)
        print("{0}".format(json.dumps(system_detail, indent=2)))
