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
from rsdclient.v1 import fabric


class FabricTest(testtools.TestCase):

    def setUp(self):
        super(FabricTest, self).setUp()
        self.client = mock.Mock()
        self.client._fabrics_path = '/redfish/v1/Fabrics'
        self.mgr = fabric.FabricManager(self.client)

    def test_list_fabric(self):
        mock_fabric_collection = mock.Mock()
        mock_fabric_collection.members_identities = \
            ('/redfish/v1/Fabrics/PCIe',)
        self.mgr.client.get_fabric_collection.return_value = \
            mock_fabric_collection
        self.mgr.client.get_fabric.return_value = fakes.FakeFabric()

        expected = (
            '+----------------------------+-------------+-------------+-------'
            '------+\n'
            '|          Identity          |     Name    | Fabric_Type | '
            'Description |\n'
            '+----------------------------+-------------+-------------+-------'
            '------+\n'
            '| /redfish/v1/Fabrics/1-ff-1 | PCIe Fabric |     PCIe    | PCIe '
            'Fabric |\n'
            '+----------------------------+-------------+-------------+-------'
            '------+')

        result = self.mgr.list()
        self.mgr.client.get_fabric_collection.assert_called_once()
        self.mgr.client.get_fabric.assert_called_once_with(
            '/redfish/v1/Fabrics/PCIe')
        self.assertEqual(str(result), expected)

    def test_show_fabric(self):
        self.client.get_fabric.return_value = fakes.FakeFabric()
        result = self.mgr.show('/redfish/v1/Fabrics/PCIe')
        expected = fakes.FAKE_FABRIC_PYTHON_DICT
        self.mgr.client.get_fabric.assert_called_once_with(
            '/redfish/v1/Fabrics/PCIe')
        self.assertEqual(result, expected)
