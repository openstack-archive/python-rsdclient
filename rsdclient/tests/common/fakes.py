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

import mock


FAKE_NODE_PYTHON_DICT = {
    "path": "/redfish/v1/Nodes/1",
    "description": "Node for testing",
    "processor_summary": {
        "count": 1,
        "model": "fake processor model",
        "health": "OK"
    },
    "composed_node_state": "allocated",
    "boot": {
        "mode": "fake boot mode",
        "enabled": "once",
        "target": "pxe",
        "allowed_values": ["pxe", "hdd"]
    },
    "uuid": "fd011520-86a2-11e7-b4d4-5d323196a3e4",
    "power_state": "on",
    "memory_summary": {
        "size_gib": 8,
        "health": "OK"
    },
    "identity": "1",
    "name": "Test"
}


class FakeProcessorSummary(object):

    def __init__(self):
        self.count = 1
        self.model = "fake processor model"
        self.health = "OK"


class FakeBoot(object):

    def __init__(self):
        self.mode = "fake boot mode"
        self.enabled = "once"
        self.target = "pxe"
        self.allowed_values = ["pxe", "hdd"]


class FakeMemorySummary(object):

    def __init__(self):
        self.size_gib = 8
        self.health = "OK"


class FakeNode(mock.Mock):

    def __init__(self, *args, **kwargs):
        super(FakeNode, self).__init__(*args, **kwargs)
        self._path = "/redfish/v1/Nodes/1"
        self.name = "Test"
        self.description = "Node for testing"
        self.identity = "1"
        self.power_state = "on"
        self.composed_node_state = "allocated"
        self.boot = FakeBoot()
        self.processor_summary = FakeProcessorSummary()
        self.memory_summary = FakeMemorySummary()
        self.uuid = "fd011520-86a2-11e7-b4d4-5d323196a3e4"

FAKE_STORAGE_PYTHON_DICT = {
    'path': '/redfish/v1/StorageServices/1-sv-1',
    'description': 'Storage Service for Testing',
    'identity': '1',
    'name': 'Storage Service',
    'redfish_version': '1.0.0',
    'remote_targets': [{
        'addresses': [{
            'iSCSI': {
                'TargetIQN': 'base_logical_volume_target',
                'TargetLUN': [{
                    'LUN': 1,
                    'LogicalDrive': {
                        '@odata.id': '/redfish/v1/Services/1/LogicalDrives/2'
                    }
                }],
                'TargetPortalIP': '10.2.0.4',
                'TargetPortalPort': 3260
            }
        }],
        'identity': '1',
        'initiator': [{'iSCSI': {'InitiatorIQN': 'ALL'}}],
        'redfish_version': '1.0.0',
        'target_type': 'iSCSITargets'
    }],
    'physical_drives': [{
        'capacity_gib': 931,
        'drive_type': 'HDD',
        'identity': '1',
        'interface': 'SATA',
        'manufacturer': 'fake manufacture',
        'model': 'ST1000NM0033-9ZM',
        'redfish_version': '1.0.0',
        'rpm': 7200,
        'serial_number': 'Z1W23Q3V'
    }],
    'logical_drives': [{
        'bootable': True,
        'capacity_gib': 5589,
        'drive_type': 'LVM',
        'identity': '2',
        'image': 'fake image',
        'mode': 'LVG',
        'protected': False,
        'redfish_version': '1.0.0',
        'snapshot': False
    }]
}


class FakeRemoteTarget(object):

    def __init__(self):
        self.addresses = [{
            'iSCSI': {
                'TargetIQN': 'base_logical_volume_target',
                'TargetLUN': [{
                    'LUN': 1,
                    'LogicalDrive': {
                        '@odata.id': '/redfish/v1/Services/1/LogicalDrives/2'
                    }
                }],
                'TargetPortalIP': '10.2.0.4',
                'TargetPortalPort': 3260
            }
        }]
        self.identity = '1'
        self.initiator = [{'iSCSI': {'InitiatorIQN': 'ALL'}}]
        self.redfish_version = '1.0.0'
        self.target_type = 'iSCSITargets'


class FakePhysicalDrive(object):

    def __init__(self):
        self.capacity_gib = 931
        self.drive_type = 'HDD'
        self.identity = '1'
        self.interface = 'SATA'
        self.manufacturer = 'fake manufacture'
        self.model = 'ST1000NM0033-9ZM'
        self.redfish_version = '1.0.0'
        self.rpm = 7200
        self.serial_number = 'Z1W23Q3V'


class FakeLogicalDrive(object):

    def __init__(self):
        self.bootable = True
        self.capacity_gib = 5589
        self.drive_type = 'LVM'
        self.identity = '2'
        self.image = 'fake image'
        self.mode = 'LVG'
        self.protected = False
        self.redfish_version = '1.0.0'
        self.snapshot = False


class FakeStorageSerice(object):

    def __init__(self):
        self._path = '/redfish/v1/StorageServices/1-sv-1'
        self.description = 'Storage Service for Testing'
        self.identity = '1'
        self.name = 'Storage Service'
        self.redfish_version = '1.0.0'
        self.remote_targets = mock.Mock()
        self.remote_targets.get_members.return_value = [FakeRemoteTarget()]
        self.physical_drives = mock.Mock()
        self.physical_drives.get_members.return_value = [FakePhysicalDrive()]
        self.logical_drives = mock.Mock()
        self.logical_drives.get_members.return_value = [FakeLogicalDrive()]


FAKE_FABRIC_PYTHON_DICT = {
    'path': '/redfish/v1/Fabrics/1-ff-1',
    'description': 'PCIe Fabric',
    'fabric_type': 'PCIe',
    'identity': 'PCIe',
    'max_zones': 5,
    'name': 'PCIe Fabric',
    'zones': [{
        'description': 'PCIe Zone 1',
        'identity': '1',
        'links': {
            'endpoint_identities': (
                '/redfish/v1/Fabrics/PCIe/Endpoints/HostRootComplex1',
                '/redfish/v1/Fabrics/PCIe/Endpoints/NVMeDrivePF2'
            )
        },
        'name': 'PCIe Zone 1'
    }],
    'endpoints': [{
        'connected_entities': [{
            'entity_link': '/redfish/v1/Chassis/PCIeSwitch1/Drives/Disk.Bay.0',
            'entity_role': 'Target',
            'entity_type': 'Drive',
            'identifiers': [{
                'name': '00000000-0000-0000-0000-000000000000',
                'name_format': 'UUID'
            }]
        }],
        'description': 'The PCIe Physical function of an 850GB NVMe drive',
        'host_reservation_memory': 1000,
        'identifiers': [{
            'name': '00000000-0000-0000-0000-000000000000',
            'name_format': 'UUID'
        }],
        'identity': 'NVMeDrivePF1',
        'name': 'NVMe Drive',
        'protocol': 'PCIe',
        'redfish_version': '1.0.2',
        'redundancy': []
    }]
}


class FakeEndpoint(object):

    def __init__(self):
        self.connected_entities = [{
            'entity_link': '/redfish/v1/Chassis/PCIeSwitch1/Drives/Disk.Bay.0',
            'entity_role': 'Target',
            'entity_type': 'Drive',
            'identifiers': [{
                'name': '00000000-0000-0000-0000-000000000000',
                'name_format': 'UUID'
            }]
        }]
        self.description = 'The PCIe Physical function of an 850GB NVMe drive'
        self.host_reservation_memory = 1000
        self.identifiers = [{
            'name': '00000000-0000-0000-0000-000000000000',
            'name_format': 'UUID'
        }]
        self.identity = 'NVMeDrivePF1'
        self.name = 'NVMe Drive'
        self.protocol = 'PCIe'
        self.redfish_version = '1.0.2'
        self.redundancy = []


class FakeZone(object):

    def __init__(self):
        self.description = 'PCIe Zone 1'
        self.identity = '1'
        self.name = 'PCIe Zone 1'
        self.links = {
            'endpoint_identities': (
                '/redfish/v1/Fabrics/PCIe/Endpoints/HostRootComplex1',
                '/redfish/v1/Fabrics/PCIe/Endpoints/NVMeDrivePF2'
            )
        }


class FakeFabric(object):

    def __init__(self):
        self._path = '/redfish/v1/Fabrics/1-ff-1'
        self.description = 'PCIe Fabric'
        self.fabric_type = 'PCIe'
        self.identity = 'PCIe'
        self.max_zones = 5
        self.name = 'PCIe Fabric'
        self.endpoints = mock.Mock()
        self.endpoints.get_members.return_value = [FakeEndpoint()]
        self.zones = mock.Mock()
        self.zones.get_members.return_value = [FakeZone()]
