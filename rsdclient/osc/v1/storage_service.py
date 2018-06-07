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


class ShowVolume(command.Command):
    """Show volume details"""

    _description = "Show volume details"

    def get_parser(self, prog_name):
        parser = super(ShowVolume, self).get_parser(prog_name)

        parser.add_argument(
            'volume',
            metavar='<volume>',
            help='ID of the volume.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        print(parsed_args.volume)
        volume_detail = rsd_client.storage_service.show_volume(
            parsed_args.volume)
        print("{0}".format(json.dumps(volume_detail, indent=2)))


class UpdateVolume(command.Command):
    """Update the volume properties"""

    _description = "Update the volume properties"

    def get_parser(self, prog_name):
        parser = super(UpdateVolume, self).get_parser(prog_name)

        parser.add_argument(
            'volume',
            metavar='<volume>',
            help='ID of the volume.')

        parser.add_argument(
            '--bootable',
            metavar='<bootable>',
            help='bootable ability of the volume.')

        parser.add_argument(
            '--erased',
            metavar='<erased config>',
            help='if the drive was erased.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        rsd_client.storage_service.update_volume(
            parsed_args.volume, parsed_args.bootable,
            parsed_args.erased)


class InitializeVolume(command.Command):
    """Initialize (erase) volume"""

    _description = "Initialize (erase) volume"

    def get_parser(self, prog_name):
        parser = super(InitializeVolume, self).get_parser(prog_name)

        parser.add_argument(
            'volume',
            metavar='<volume>',
            help='ID of the volume.')

        parser.add_argument(
            '--init_type',
            metavar='<init type>',
            help='Type of volume initialize (erase) process.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        rsd_client.storage_service.initialize_volume(
            parsed_args.volume, parsed_args.init_type)


class CreateVolume(command.Command):
    """Create a new volume"""

    _description = "Create a new volume"

    def get_parser(self, prog_name):
        parser = super(CreateVolume, self).get_parser(prog_name)
        parser.add_argument(
            'storageservice',
            metavar='<storage service>',
            help='ID of the storage service.')

        parser.add_argument(
            '--capacity',
            type=int,
            metavar='<volume capacity>',
            help='Capacity of the volume.')

        parser.add_argument(
            '--access_capabilities',
            metavar='<storage service>',
            help='List of volume access capabilities, e.g. [\'Read\', '
                 '\'Write\', \'WriteOnce\', \'Append\', \'Streaming\']')

        parser.add_argument(
            '--capacity_sources',
            metavar='<storage service>',
            help='JSON for volume providing source.')

        parser.add_argument(
            '--replica_infos',
            metavar='<storage service>',
            help='JSON for volume replica infos.')

        parser.add_argument(
            '--bootable',
            metavar='<storage service>',
            help='Determines if the volume should be bootable.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        rsd_client.storage_service.create_volume(
            parsed_args.storageservice, parsed_args.capacity,
            parsed_args.access_capabilities, parsed_args.capacity_sources,
            parsed_args.replica_infos, parsed_args.bootable)


class DeleteVolume(command.Command):
    """Delete a volume"""

    _description = "Delete a volume"

    def get_parser(self, prog_name):
        parser = super(DeleteVolume, self).get_parser(prog_name)

        parser.add_argument(
            'volume',
            metavar='<volume>',
            help='ID of the volume.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        rsd_client.storage_service.delete_volume(parsed_args.volume)


class ListDrives(command.Command):
    """List all drives of one storage service."""

    _description = "List all drives of one storage service"

    def get_parser(self, prog_name):
        parser = super(ListDrives, self).get_parser(prog_name)
        parser.add_argument(
            'storageservice',
            metavar='<storage service>',
            help='ID of the storage service.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        drive_list = rsd_client.storage_service.list_drive(
            parsed_args.storageservice)
        print(drive_list)
