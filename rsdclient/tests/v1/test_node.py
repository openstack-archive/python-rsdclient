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
import testtools

from rsdclient.tests.common import fakes
from rsdclient.v1 import node


class NodeTest(testtools.TestCase):

    def setUp(self):
        super(NodeTest, self).setUp()
        self.client = mock.Mock()
        self.client._nodes_path = '/redfish/v1/Nodes'
        self.mgr = node.NodeManager(self.client)

    def test_compose_node(self):
        mock_node_collection = mock.Mock()
        mock_node_collection.compose_node.return_value = '/redfish/v1/Nodes/1'
        self.client.get_node_collection.return_value = mock_node_collection
        result = self.mgr.compose(name='fake_name',
                                  description='fake_description')
        self.mgr.client.get_node_collection.assert_called_once()
        mock_node_collection.compose_node.assert_called_once_with(
            name='fake_name', description='fake_description',
            processor_req=None, memory_req=None, remote_drive_req=None,
            local_drive_req=None, ethernet_interface_req=None)
        self.assertEqual(result, '1')

    def test_delete_node(self):
        node_id = '1'
        mock_node = mock.Mock()
        self.client.get_node.return_value = mock_node
        self.mgr.delete(node_id)
        self.mgr.client.get_node.assert_called_once_with('/redfish/v1/Nodes/1')
        mock_node.delete_node.assert_called_once()

    def test_show_node(self):
        node = fakes.FakeNode()
        node.get_allowed_attach_endpoints.return_value = \
            ('/redfish/v1/Chassis/3-c-1/Drives/3-c-1-d-1',)
        node.get_allowed_detach_endpoints.return_value = ()
        node.get_allowed_node_boot_source_values.return_value = ('pxe', 'hdd')
        node.get_allowed_reset_node_values.return_value = ('on', 'force off')
        self.client.get_node.return_value = node

        result = self.mgr.show('1')
        # Pop out mock.Mock variable 'method_calls'
        result.pop('method_calls')
        expected = fakes.FAKE_NODE_PYTHON_DICT
        expected.update(
            {
                "allowed_attach_endpoints":
                    ['/redfish/v1/Chassis/3-c-1/Drives/3-c-1-d-1'],
                "allowed_detach_endpoints": [],
                "allowed_boot_source": ["pxe", "hdd"],
                "allowed_reset_node_values": ["on", "force off"]
            })
        self.assertEqual(result, expected)

    def test_list_node(self):
        mock_node_collection = mock.Mock()
        mock_node_collection.members_identities = ('/redfish/v1/Nodes/1',)
        self.mgr.client.get_node_collection.return_value = mock_node_collection
        self.mgr.client.get_node.return_value = fakes.FakeNode()

        expected = '+----------+------+--------------------------------------'\
                   '+------------------+\n'\
                   '| Identity | Name |                 UUID                 '\
                   '|   Description    |\n'\
                   '+----------+------+--------------------------------------'\
                   '+------------------+\n'\
                   '|    1     | Test | fd011520-86a2-11e7-b4d4-5d323196a3e4 '\
                   '| Node for testing |\n'\
                   '+----------+------+--------------------------------------'\
                   '+------------------+'

        result = self.mgr.list()
        self.mgr.client.get_node_collection.assert_called_once()
        self.mgr.client.get_node.assert_called_once_with('/redfish/v1/Nodes/1')
        self.assertEqual(str(result), expected)

    def test_attach(self):
        node_id = '1'
        mock_node = mock.Mock()
        self.client.get_node.return_value = mock_node
        self.mgr.attach(node_id, 'fake uri', 10)
        self.mgr.client.get_node.assert_called_once_with('/redfish/v1/Nodes/1')
        mock_node.attach_endpoint.assert_called_once_with('fake uri', 10)

    def test_detach(self):
        node_id = '1'
        mock_node = mock.Mock()
        self.client.get_node.return_value = mock_node
        self.mgr.detach(node_id, 'fake uri')
        self.mgr.client.get_node.assert_called_once_with('/redfish/v1/Nodes/1')
        mock_node.detach_endpoint.assert_called_once_with('fake uri')
