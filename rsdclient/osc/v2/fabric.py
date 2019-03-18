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


class ShowEndpoint(command.Command):
    """Show endpoint details"""

    _description = "Show endpoint details"

    def get_parser(self, prog_name):
        parser = super(ShowEndpoint, self).get_parser(prog_name)

        parser.add_argument(
            'endpoint',
            metavar='<endpoint>',
            help='ID of the endpoint.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        endpoint_detail = rsd_client.fabric.show_endpoint(
            parsed_args.endpoint)
        print("{0}".format(json.dumps(endpoint_detail, indent=2)))


class CreateEndpoint(command.Command):
    """Create a endpoint."""

    _description = "Create a endpoint"

    def get_parser(self, prog_name):
        parser = super(CreateEndpoint, self).get_parser(prog_name)
        # NOTE: All arguments are positional and, if not provided
        # with a default, required.
        parser.add_argument('--fabric',
                            metavar='<fabric>',
                            help='ID of the fabric to create a endpoint.')
        parser.add_argument(
            '--connected_entities',
            dest='connected_entities',
            type=json.loads,
            metavar='<connected entities>',
            help=('Array of all the entities which this endpoint allows access'
                  ' to.\n\n'
                  'For example:\n'
                  '[{'
                  '  "EntityType": "Drive",\n'
                  '  "EntityRole": "Target",\n'
                  '  "EntityLink": {\n'
                  '    "@odata.id": "/redfish/v1/Chassis/PCIeSwitch1/Drives/'
                  'Disk.Bay.0"\n'
                  '  }\n'
                  '}]'))
        parser.add_argument(
            '--identifiers',
            dest='identifiers',
            type=json.loads,
            metavar='<identifiers>',
            help=('Identifiers for this endpoint shall be unique in the '
                  'context of other endpoints that can reached over the '
                  'connected network.\n\n'
                  'For example:\n'
                  '[{\n'
                  '  "DurableName": "nqn.2014-08.org.nvmexpress:NVMf:uuid:'
                  '397f9b78-7e94-11e7-9ea4-001e67dfa170",\n'
                  '  "DurableNameFormat": "NQN"\n'
                  '}]'))
        parser.add_argument(
            '--protocol',
            metavar='<protocol>',
            help=('The protocol this endpoint uses to communicate with other '
                  'endpoints on this fabric.'))
        parser.add_argument(
            '--pci_id',
            dest='pci_id',
            type=json.loads,
            metavar='<pci id>',
            help='Array of PCI ID of the endpoint.')
        parser.add_argument(
            '--host_reservation_memory_bytes',
            metavar='<host_reservation_memory_bytes>',
            type=int,
            help=('The amount of memory, in bytes, that the Host should '
                  'allocate to connect to this endpoint.'))
        parser.add_argument(
            '--ip_transport_details',
            dest='ip_transport_details',
            type=json.loads,
            metavar='<ip transport details>',
            help=('Array of each IP transport supported by this endpoint.\n\n'
                  'For example:\n'
                  '[{\n'
                  '  "TransportProtocol": "RoCEv2",\n'
                  '  "IPv4Address": {\n'
                  '    "Address": "192.168.0.10"\n'
                  '  },\n'
                  '  "IPv6Address": {},\n'
                  '  "Port": 1023\n'
                  '}]'))
        parser.add_argument(
            '--links',
            dest='links',
            type=json.loads,
            metavar='<links>',
            help=('The links to other resources that are related to this '
                  'resource.'))
        parser.add_argument(
            '--oem',
            dest='oem',
            type=json.loads,
            metavar='<oem>',
            help=('The Oem specific fields that are related to this '
                  'resource.'))

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd

        endpoint_id = rsd_client.fabric.create_endpoint(
            parsed_args.fabric, parsed_args.connected_entities,
            parsed_args.identifiers, parsed_args.protocol, parsed_args.pci_id,
            parsed_args.host_reservation_memory_bytes,
            parsed_args.ip_transport_details, parsed_args.links,
            parsed_args.oem)
        print("Endpoint {0} has been created.".format(endpoint_id))
