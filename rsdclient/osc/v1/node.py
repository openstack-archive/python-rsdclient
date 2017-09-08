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


ARGUMENTS_NAME_MAPPING = {
    'name': 'Name',
    'description': 'Description',
    'processor': 'Processors',
    'memory': 'Memory',
    'remote_drives': 'RemoteDrives',
    'local_drives': 'LocalDrives',
    'ethernet': 'EthernetInterfaces'
}


class ComposeNode(command.Command):
    _description = "Compose a Node"

    def get_parser(self, prog_name):
        parser = super(ComposeNode, self).get_parser(prog_name)
        # NOTE: All arguments are positional and, if not provided
        # with a default, required.
        parser.add_argument('--name',
                            metavar='<name>',
                            help='Name of the composed node.')
        parser.add_argument('--description',
                            metavar='<description>',
                            help='Description of the composed node.')
        parser.add_argument(
            '--processor',
            dest='processor',
            type=json.loads,
            metavar='<processor requirements>',
            help=('Array of requirements for processor for composed node. Each'
                  ' processor requirement may contain one or more optional '
                  'attributes:\n'
                  '  - Model: Type String, Processor model that should be used'
                  ' for composed node (exact model name)\n\n'
                  '  - TotalCores: Type Int, Minimum number of processor cores'
                  '  - AchievableSpeedMHz: Type Int, Minimum achievable '
                  'processor operating frequency.\n\n'
                  '  - InstructionSet: Type String, Processor supported '
                  'instruction set, such as "x86", "x86-64", "IA-64", '
                  '"ARM-A32", "ARM-A64", "MIPS32", "MIPS64", "OEM"\n\n'
                  '  - Resource: Object Reference to a particular processor '
                  'that should be used in composed node\n\n'
                  '  - Chassis: Object Link to chassis object within this '
                  'processor should be contained.\n\n'
                  '  - Brand: Type String, Brand of CPU that should be used to'
                  ' allocate node.'
                  '  - Capabilities: Array of strings describing processor '
                  'capabilities (like reported in /proc/cpuinfo flags), such '
                  'as "sse", "avx", etc.\n\n'
                  'For example:\n'
                  '[{\n'
                  '  "Model": "Multi-Core Intel(R) Xeon(R) processor 7xxx '
                  'Series",\n'
                  '  "TotalCores": 2,\n'
                  '  "AchievableSpeedMHz": 2000,\n'
                  '  "InstructionSet": "x86",\n'
                  '  "Oem": {\n'
                  '    "Brand": "E5",\n'
                  '    "Capabilities": [ "sse" ],\n'
                  '  },\n'
                  '  "Resource": {\n'
                  '    "@odata.id": "/redfish/v1/Systems/System1/Processors'
                  '/CPU1"\n'
                  '  }\n'
                  '}]'))
        parser.add_argument(
            '--memory',
            dest='memory',
            type=json.loads,
            metavar='<memory requirements>',
            help=('Array of requirements for memory for composed node. Each '
                  'memory requirement may contain one or more optional '
                  'attributes:\n'
                  '  - CapacityMiB: Type Int, Minimum memory capacity '
                  'requested for composed node\n\n'
                  '  - MemoryDeviceType: Type String, Type details of DIMM, '
                  'such as "DDR3", "DDR4"\n\n'
                  '  - SpeedMHz: Type Int, Minimum supported memory speed\n\n'
                  ' - Manufacturer: Type String, Requested memory '
                  'manufacturer\n\n'
                  '  - DataWidthBits: Type Int, Requested memory data width in'
                  ' bits\n\n'
                  '  - Resource: Object Reference to a particular memory '
                  'module that should be used in composed node\n\n'
                  '  - Chassis: Object Link to chassis object within this '
                  'memory DIMM should be contained\n\n'
                  'For example:\n'
                  '[{\n'
                  '  "CapacityMiB": 16000,\n'
                  '  "MemoryDeviceType": "DDR3",\n'
                  '  "SpeedMHz": 1600,\n'
                  '  "Manufacturer": "Intel",\n'
                  '  "DataWidthBits": 64,\n'
                  '  "Resource": {\n'
                  '    "@odata.id": "/redfish/v1/Systems/System1/Memory/'
                  'Dimm1"\n'
                  '  },\n'
                  '  "Chassis": {\n'
                  '    "@odata.id": "/redfish/v1/Chassis/Rack1"\n'
                  '  }\n'
                  '}]'))
        parser.add_argument(
            '--remote-drives',
            dest='remote_drives',
            type=json.loads,
            metavar='<remote drives requirements>',
            help=('Array of requirements for remote drives that should be '
                  'created/connected to composed node. Each remote drives '
                  'requirement may contain one or more optional attributes:\n'
                  '  - CapacityGiB: Type Int, Minimum drive capacity requested'
                  ' for composed node\n\n'
                  '  - iSCSIAddress: Type String, Defines TargetIQN of '
                  'RemoteTarget to be set for new Remote Target (should be '
                  'unique in PODM)\n\n'
                  '  - Master: Object Defines master logical volume that '
                  'should be taken to create new remote target. It contains '
                  'following two properties: Type and Resource\n\n'
                  '  - Type: Type String, Type of replication of master drive:'
                  ' Clone - volume should be cloned, Snapshot - Copy on Write '
                  'should be created from indicated volume\n\n'
                  '  - Resource: Object Reference to logical volume that '
                  'should be used as master for replication\n\n'
                  'For example:\n'
                  '[{\n'
                  '  "CapacityGiB": 80,\n'
                  '  "iSCSIAddress": "iqn.oem.com:fedora21",\n'
                  '  "Master": {\n'
                  '    "Type": "Snapshot",\n'
                  '    "Resource": {\n'
                  '      "@odata.id": "/redfish/v1/Services/RSS1/LogicalDrives'
                  '/sda1"\n'
                  '    }\n'
                  '  }\n'
                  '}]'))
        parser.add_argument(
            '--local-drives',
            dest='local_drives',
            type=json.loads,
            metavar='<local drives requirements>',
            help=('Array of requirements for local drives for composed node. '
                  'Each local drives requirement may contain one or more '
                  'optional attributes:\n'
                  '  - CapacityGiB: Type Int, Minimum drive capacity requested'
                  ' for composed node\n\n'
                  '  - Type: Type String, Drive type: "HDD", "SSD"\n\n'
                  '  - MinRPM: Type Int, Minimum rotation speed of requested '
                  'drive\n\n'
                  '  - SerialNumber: Type String, Serial number of requested '
                  'drive\n\n'
                  '  - Interface: Type String, Interface of requested drive: '
                  '"SAS", "SATA", "NVMe"\n\n'
                  '  - Resource: Object Reference to particular local drive '
                  'that should be used in composed node\n\n'
                  '  - Chassis: Object Link to chassis object within this '
                  'drive should be contained\n\n'
                  '  - FabricSwitch: Type Boolean, Determine if local drive '
                  'should be connected using fabric switch or local '
                  'connected\n\n'
                  'For example:\n'
                  '[{\n'
                  '  "CapacityGiB": 500,\n'
                  '  "Type": "HDD",\n'
                  '  "MinRPM": 5400,\n'
                  '  "SerialNumber": "12345678",\n'
                  '  "Interface": "SATA",\n'
                  '  "Resource": {\n'
                  '    "@odata.id": "redfish/v1/Chassis/Blade1/Drives/Disk1"\n'
                  '  },\n'
                  '  "FabricSwitch": false\n'
                  '}]'))
        parser.add_argument(
            '--ethernet',
            dest='ethernet',
            type=json.loads,
            metavar='<ethernet requirements>',
            help=('Array of requirements for Ethernet interfaces of composed '
                  'node. Each Ethernet interface requirement may contain one '
                  'or more optional attributes:\n'
                  '  - SpeedMbps: Type Int, Minimum speed of Ethernet '
                  'interface requested for composed node\n\n'
                  '  - VLANs: Type Array, Array of VLANs that should be '
                  'configured on connected switch port for composed node for '
                  'given Ethernet interface in the following format: VLANId - '
                  'number indicating VLAN Id, Tagged - Boolean value '
                  'describing if given VLAN is tagged\n\n'
                  '  - PrimaryVLAN: Type Int, Primary VLAN ID that should be '
                  'set for a given Ethernet Interface\n\n'
                  '  - Resource: Object Reference to a particular Ethernet '
                  'interface that should be used in composed node\n\n'
                  '  - Chassis: Object Link to chassis object within this '
                  'network interface should be contained\n\n'
                  'For example:\n'
                  '[{\n'
                  '  "SpeedMbps": 1000,\n'
                  '  "PrimaryVLAN": 100,\n'
                  '  "VLANs": [{\n'
                  '    "VLANId": 100,\n'
                  '    "Tagged": false\n'
                  '  }],\n'
                  '  "Resource": {\n'
                  '    "@odata.id": "/redfish/v1/Systems/System1/'
                  'EthernetInterfaces/LAN1"\n'
                  '  }\n'
                  '}]'))
        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        args = {}
        for i in ARGUMENTS_NAME_MAPPING:
            if getattr(parsed_args, i):
                args[ARGUMENTS_NAME_MAPPING[i]] = getattr(parsed_args, i)
        node_id = rsd_client.node.compose(args)
        print("Node {0} has been composed.".format(node_id))


class DeleteNode(command.Command):
    _description = "Delete a Node"

    def get_parser(self, prog_name):
        parser = super(DeleteNode, self).get_parser(prog_name)
        parser.add_argument(
            'node',
            nargs='+',
            metavar='<node>',
            help='ID of the node(s) to delete.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        for node in parsed_args.node:
            rsd_client.node.delete(node)
            print("Node {0} has been deleted.".format(node))


class ShowNode(command.Command):
    _description = "Display node details"

    def get_parser(self, prog_name):
        parser = super(ShowNode, self).get_parser(prog_name)
        parser.add_argument(
            'node',
            metavar='<node>',
            help='ID of the node.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        node_detail = rsd_client.node.show(parsed_args.node)
        print("{0}".format(json.dumps(node_detail, indent=2)))


class ListNode(command.Command):
    _description = "List all composed nodes"

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        node_list = rsd_client.node.list()
        print(node_list)


class AttachEndpoint(command.Command):
    _description = "Attach drive to existing composed node"

    def get_parser(self, prog_name):
        parser = super(AttachEndpoint, self).get_parser(prog_name)
        parser.add_argument(
            'node',
            metavar='<node>',
            help='ID of the node.')
        parser.add_argument(
            '--resource',
            metavar='<resource uri>',
            help='URI of the specific resource to attach to node.')
        parser.add_argument(
            '--capacity',
            metavar='<size>',
            type=int,
            help='Required storage capacity in GiB.')
        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        rsd_client.node.attach(parsed_args.node, parsed_args.resource,
                               parsed_args.capacity)
