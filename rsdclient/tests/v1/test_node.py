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

from rsdclient.v1 import node


class ClusterManagerTest(testtools.TestCase):

    def setUp(self):
        super(ClusterManagerTest, self).setUp()
        self.client = mock.Mock()
        self.mgr = node.NodeManager(self.client)

    def test_compose_node(self):
        mock_node_collection = mock.Mock()
        self.client.get_node_collection.return_value = mock_node_collection
        self.mgr.compose({'Name': 'fake_name'})
        self.mgr.client.get_node_collection.assert_called_once()
        mock_node_collection.compose_node.assert_called_once_with(
            {'Name': 'fake_name'})

    def test_delete_node(self):
        node_uri = '/redfish/v1/Nodes/1'
        mock_node = mock.Mock()
        self.client.get_node.return_value = mock_node
        self.mgr.delete(node_uri)
        self.mgr.client.get_node.assert_called_once_with(node_uri)
        mock_node.delete_node.assert_called_once()
