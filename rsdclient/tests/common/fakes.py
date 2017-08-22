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
