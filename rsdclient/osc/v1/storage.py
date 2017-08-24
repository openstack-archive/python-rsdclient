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


class ListStorage(command.Command):
    _description = "List all storage services"

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        storage_service_list = rsd_client.storage.list()
        print(storage_service_list)


class ShowStorage(command.Command):
    _description = "Display storage service details"

    def get_parser(self, prog_name):
        parser = super(ShowStorage, self).get_parser(prog_name)
        parser.add_argument(
            'storage',
            metavar='<storage>',
            help='ID of the storage service.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        storage_detail = rsd_client.storage.show(parsed_args.storage)
        print("{0}".format(json.dumps(storage_detail, indent=2)))
