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
from rsdclient.v1 import storage_service


class StorageServiceTest(testtools.TestCase):

    def setUp(self):
        super(StorageServiceTest, self).setUp()
        self.client = mock.Mock()
        self.client._storage_service_path = '/redfish/v1/Services'
        self.mgr = storage_service.StorageServiceManager(self.client)

    def test_list_storage(self):
        mock_storage_collection = mock.Mock()
        mock_storage_collection.members_identities = \
            ('/redfish/v1/Services/1',)
        self.mgr.client.get_storage_service_collection.return_value = \
            mock_storage_collection
        self.mgr.client.get_storage_service.return_value = \
            fakes.FakeStorageSerice()

        expected = (
            '+----------+-----------------+-----------------------------+\n'
            '| Identity |       Name      |         Description         |\n'
            '+----------+-----------------+-----------------------------+\n'
            '|    1     | Storage Service | Storage Service for Testing |\n'
            '+----------+-----------------+-----------------------------+')

        result = self.mgr.list()
        self.mgr.client.get_storage_service_collection.assert_called_once()
        self.mgr.client.get_storage_service.assert_called_once_with(
            '/redfish/v1/Services/1')
        self.assertEqual(str(result), expected)

    def test_show_storage(self):
        self.client.get_storage_service.return_value = \
            fakes.FakeStorageSerice()
        result = self.mgr.show('1')
        expected = fakes.FAKE_STORAGE_PYTHON_DICT
        self.assertEqual(result, expected)
