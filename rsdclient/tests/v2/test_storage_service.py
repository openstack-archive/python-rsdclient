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
from rsdclient.v2 import storage_service


class StorageServiceTest(testtools.TestCase):

    def setUp(self):
        super(StorageServiceTest, self).setUp()
        self.client = mock.Mock()
        self.client._storage_service_path = '/redfish/v1/StorageServices'
        self.mgr = storage_service.StorageServiceManager(self.client)

    def test__extract_storage_service_uri(self):
        self.assertIsNone(self.mgr._extract_storage_service_uri('invalid uri'))
        self.assertEqual(
            '/redfish/v1/StorageServices/1-sv-1',
            self.mgr._extract_storage_service_uri(
                '/redfish/v1/StorageServices/1-sv-1/Volumes/1-sv-1-vl-1'))

    def test_list_storage(self):
        mock_storage_collection = mock.Mock()
        mock_storage_collection.members_identities = \
            ('/redfish/v1/Services/1',)
        self.mgr.client.get_storage_service_collection.return_value = \
            mock_storage_collection
        self.mgr.client.get_storage_service.return_value = \
            fakes.FakeStorageSerice()

        expected = (
            '+------------------------------------+-----------------+---------'
            '--------------------+\n'
            '|              Identity              |       Name      |         '
            'Description         |\n'
            '+------------------------------------+-----------------+---------'
            '--------------------+\n'
            '| /redfish/v1/StorageServices/1-sv-1 | Storage Service | Storage '
            'Service for Testing |\n'
            '+------------------------------------+-----------------+---------'
            '--------------------+')

        result = self.mgr.list()
        self.mgr.client.get_storage_service_collection.assert_called_once()
        self.mgr.client.get_storage_service.assert_called_once_with(
            '/redfish/v1/Services/1')
        self.assertEqual(str(result), expected)

    def test_show_storage(self):
        self.client.get_storage_service.return_value = \
            fakes.FakeStorageSerice()
        result = self.mgr.show('/redfish/v1/StorageServices/1-sv-1')
        expected = fakes.FAKE_STORAGE_PYTHON_DICT
        self.assertEqual(result, expected)
        self.mgr.client.get_storage_service.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1')

    def test_list_volume(self):
        mock_storage = mock.Mock()
        self.client.get_storage_service.return_value = mock_storage
        mock_storage.volumes.get_members.return_value = ()

        self.mgr.list_volume('/redfish/v1/StorageServices/1-sv-1')
        self.mgr.client.get_storage_service.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1')
        mock_storage.volumes.get_members.assert_called_once()

    def test_show_volume(self):
        mock_storage = mock.Mock()
        self.client.get_storage_service.return_value = mock_storage

        self.mgr.show_volume(
            '/redfish/v1/StorageServices/1-sv-1/Volumes/1-sv-1-vl-1')
        self.mgr.client.get_storage_service.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1')
        mock_storage.volumes.get_member.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1/Volumes/1-sv-1-vl-1')

    def test_update_volume(self):
        mock_storage = mock.Mock()
        self.client.get_storage_service.return_value = mock_storage
        mock_volume = mock.Mock()
        mock_storage.volumes.get_member.return_value = mock_volume

        self.mgr.update_volume(
            '/redfish/v1/StorageServices/1-sv-1/Volumes/1-sv-1-vl-1',
            bootable='True')
        self.mgr.client.get_storage_service.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1')
        mock_storage.volumes.get_member.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1/Volumes/1-sv-1-vl-1')
        mock_volume.update.assert_called_once_with(True, None)

        self.mgr.client.reset_mock()
        mock_storage.reset_mock()
        mock_volume.reset_mock()
        self.mgr.update_volume(
            '/redfish/v1/StorageServices/1-sv-1/Volumes/1-sv-1-vl-1',
            erased='True')
        self.mgr.client.get_storage_service.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1')
        mock_storage.volumes.get_member.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1/Volumes/1-sv-1-vl-1')
        mock_volume.update.assert_called_once_with(None, True)

        self.mgr.client.reset_mock()
        mock_storage.reset_mock()
        mock_volume.reset_mock()
        self.mgr.update_volume(
            '/redfish/v1/StorageServices/1-sv-1/Volumes/1-sv-1-vl-1',
            bootable='True', erased='True')
        self.mgr.client.get_storage_service.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1')
        mock_storage.volumes.get_member.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1/Volumes/1-sv-1-vl-1')
        mock_volume.update.assert_called_once_with(True, True)

    def test_initialize_volume(self):
        mock_storage = mock.Mock()
        self.client.get_storage_service.return_value = mock_storage
        mock_volume = mock.Mock()
        mock_storage.volumes.get_member.return_value = mock_volume

        self.mgr.initialize_volume(
            '/redfish/v1/StorageServices/1-sv-1/Volumes/1-sv-1-vl-1',
            init_type='Fast')
        self.mgr.client.get_storage_service.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1')
        mock_storage.volumes.get_member.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1/Volumes/1-sv-1-vl-1')
        mock_volume.initialize.assert_called_once_with('Fast')

    def test_create_volume(self):
        mock_storage = mock.Mock()
        self.client.get_storage_service.return_value = mock_storage

        self.mgr.create_volume(
            '/redfish/v1/StorageServices/1-sv-1', capacity=1024,
            access_capabilities=['Read'], capacity_sources=[],
            replica_infos=[], bootable=True)
        self.mgr.client.get_storage_service.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1')
        mock_storage.volumes.create_volume.assert_called_once_with(
            1024, ['Read'], [], [], True)

    def test_delete_volume(self):
        mock_storage = mock.Mock()
        self.client.get_storage_service.return_value = mock_storage
        mock_volume = mock.Mock()
        mock_storage.volumes.get_member.return_value = mock_volume

        self.mgr.delete_volume(
            '/redfish/v1/StorageServices/1-sv-1/Volumes/1-sv-1-vl-1')
        self.mgr.client.get_storage_service.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1')
        mock_storage.volumes.get_member.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1/Volumes/1-sv-1-vl-1')
        mock_volume.delete.assert_called_once()

    def test_list_drive(self):
        mock_storage = mock.Mock()
        self.client.get_storage_service.return_value = mock_storage
        mock_storage.drives.get_members.return_value = ()

        self.mgr.list_drive('/redfish/v1/StorageServices/1-sv-1')
        self.mgr.client.get_storage_service.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1')
        mock_storage.drives.get_members.assert_called_once()

    def test_show_drive(self):
        mock_storage = mock.Mock()
        mock_storage.drives.members_identities = (
            '/redfish/v1/Chassis/1-c-1/Drives/1-c-1-d-1',)
        mock_storage_col = mock.Mock()
        mock_storage_col.get_members.return_value = (mock_storage,)
        self.client.get_storage_service_collection.return_value = \
            mock_storage_col

        self.mgr.show_drive('/redfish/v1/Chassis/1-c-1/Drives/1-c-1-d-1')
        mock_storage_col.get_members.assert_called_once()
        mock_storage.drives.get_member.assert_called_once_with(
            '/redfish/v1/Chassis/1-c-1/Drives/1-c-1-d-1')

    def test_list_storage_pool(self):
        mock_storage = mock.Mock()
        self.client.get_storage_service.return_value = mock_storage
        mock_storage.storage_pools.get_members.return_value = ()

        self.mgr.list_storage_pool('/redfish/v1/StorageServices/1-sv-1')
        self.mgr.client.get_storage_service.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1')
        mock_storage.storage_pools.get_members.assert_called_once()

    def test_show_storage_pool(self):
        mock_storage = mock.Mock()
        self.client.get_storage_service.return_value = mock_storage

        self.mgr.show_storage_pool(
            '/redfish/v1/StorageServices/1-sv-1/StoragePools/1-sv-1-sp-1')
        self.mgr.client.get_storage_service.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1')
        mock_storage.storage_pools.get_member.assert_called_once_with(
            '/redfish/v1/StorageServices/1-sv-1/StoragePools/1-sv-1-sp-1')
