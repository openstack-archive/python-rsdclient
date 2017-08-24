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

from rsdclient.common import utils


FAKE_NODE_PYTHON_DICT = {
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


class FakeNode(object):

    def __init__(self):
        self.name = "Test"
        self.description = "Node for testing"
        self.identity = "1"
        self.power_state = "on"
        self.composed_node_state = "allocated"
        self.boot = FakeBoot()
        self.processor_summary = FakeProcessorSummary()
        self.memory_summary = FakeMemorySummary()
        self.uuid = "fd011520-86a2-11e7-b4d4-5d323196a3e4"


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
        self.description = 'Storage Service for Testing'
        self.identity = '1'
        self.name = 'Storage Service'
        self.redfish_version = '1.0.0'
        self.remote_targets = [FakeRemoteTarget()]
        self.physical_drives = [FakePhysicalDrive()]
        self.logical_drives = [FakeLogicalDrive()]


FAKE_STORAGE_PYTHON_DICT = utils.extract_attr(FakeStorageSerice())
