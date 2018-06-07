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


class ListStorageServices(command.Command):
    """List all storage services."""

    _description = "List all storage services"

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        storage_service_list = rsd_client.storage_service.list()
        print(storage_service_list)


class ShowStorageServices(command.Command):
    """Show storage service details"""

    _description = "Show storage service details"

    def get_parser(self, prog_name):
        parser = super(ShowStorageServices, self).get_parser(prog_name)
        parser.add_argument(
            'storageservice',
            metavar='<storage service>',
            help='ID of the storage service.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        storage_detail = rsd_client.storage_service.show(
            parsed_args.storageservice)
        print("{0}".format(json.dumps(storage_detail, indent=2)))


class ListVolumes(command.Command):
    """List all volumes of one storage service."""

    _description = "List all volumes of one storage service"

    def get_parser(self, prog_name):
        parser = super(ListVolumes, self).get_parser(prog_name)
        parser.add_argument(
            'storageservice',
            metavar='<storage service>',
            help='ID of the storage service.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        volume_list = rsd_client.storage_service.list_volume(
            parsed_args.storageservice)
        print(volume_list)
