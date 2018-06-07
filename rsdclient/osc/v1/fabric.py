#   Copyright 2017 Intel, Inc.
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


class ListFabric(command.Command):
    """List all fabrics."""

    _description = "List all Fabrics"

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        fabric_list = rsd_client.fabric.list()
        print(fabric_list)


class ShowFabric(command.Command):
    """Show fabric details."""

    _description = "Display fabric details"

    def get_parser(self, prog_name):
        parser = super(ShowFabric, self).get_parser(prog_name)
        parser.add_argument(
            'fabric',
            metavar='<fabric>',
            help='ID of the fabric.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        fabric_detail = rsd_client.fabric.show(parsed_args.fabric)
        print("{0}".format(json.dumps(fabric_detail, indent=2)))


class ListEndpoint(command.Command):
    """List all endpoints of one fabric."""

    _description = "List all endpoints of one fabric"

    def get_parser(self, prog_name):
        parser = super(ListEndpoint, self).get_parser(prog_name)
        parser.add_argument(
            'fabric',
            metavar='<fabric>',
            help='ID of the fabric.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        endpoint_list = rsd_client.fabric.list_endpoint(parsed_args.fabric)
        print(endpoint_list)
