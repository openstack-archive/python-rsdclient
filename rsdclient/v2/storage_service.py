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

from rsdclient.common import base
from rsdclient.common import utils


class StorageServiceManager(base.Manager):
    _resource_name = 'storages'

    def __init__(self, *args, **kwargs):
        super(StorageServiceManager, self).__init__(*args, **kwargs)
        self.storage_service_path = self.client._storage_service_path

    def _extract_storage_service_uri(self, uri):
        if not uri.startswith(self.storage_service_path):
            return None

        return uri[:uri.find('/', len(self.storage_service_path) + 1)]

    def list(self):
        storage_service_collection = \
            self.client.get_storage_service_collection()
        storages = [utils.extract_attr(self.client.
                    get_storage_service(storage_uri))
                    for storage_uri in storage_service_collection.
                    members_identities]
        storage_info_table = utils.print_dict(
            storages, ["Identity", "Name", "Description"])
        return storage_info_table

    def show(self, storage_uri):
        storage = self.client.get_storage_service(storage_uri)
        storage_dict = utils.extract_attr(storage)

        # Append the member link of sub-resource
        storage_dict['drives'] = storage.drives.members_identities
        storage_dict['storage_pools'] = \
            storage.storage_pools.members_identities
        storage_dict['volumes'] = storage.volumes.members_identities
        storage_dict['endpoints'] = storage.endpoints.members_identities

        return storage_dict

    def list_volume(self, storage_uri):
        storage = self.client.get_storage_service(storage_uri)

        volume_collection = storage.volumes.get_members()
        volumes_info = [utils.extract_attr(volume)
                        for volume in volume_collection]
        volume_info_table = utils.print_dict(
            volumes_info, ["Identity", "Name", "Description"])
        return volume_info_table

    def show_volume(self, volume_uri):
        storage = self.client.get_storage_service(
            self._extract_storage_service_uri(volume_uri))
        volume = storage.volumes.get_member(volume_uri)

        return utils.extract_attr(volume)

    def update_volume(self, volume_uri, bootable=None, erased=None):
        storage = self.client.get_storage_service(
            self._extract_storage_service_uri(volume_uri))
        volume = storage.volumes.get_member(volume_uri)

        if bootable is not None:
            bootable = bool(bootable)
        if erased is not None:
            erased = bool(erased)

        volume.update(bootable, erased)

    def initialize_volume(self, volume_uri, init_type):
        storage = self.client.get_storage_service(
            self._extract_storage_service_uri(volume_uri))
        volume = storage.volumes.get_member(volume_uri)

        volume.initialize(init_type)

    def create_volume(self, storage_uri, capacity, access_capabilities=None,
                      capacity_sources=None, replica_infos=None,
                      bootable=None):
        storage = self.client.get_storage_service(storage_uri)
        volume_col = storage.volumes

        volume_col.create_volume(capacity, access_capabilities,
                                 capacity_sources, replica_infos,
                                 bootable)

    def delete_volume(self, volume_uri):
        storage = self.client.get_storage_service(
            self._extract_storage_service_uri(volume_uri))
        volume = storage.volumes.get_member(volume_uri)

        volume.delete()

    def list_drive(self, storage_uri):
        storage = self.client.get_storage_service(storage_uri)
        drive_collection = storage.drives.get_members()

        drives_info = [utils.extract_attr(drive)
                       for drive in drive_collection]
        drive_info_table = utils.print_dict(
            drives_info, ["Identity", "Name", "Description"])
        return drive_info_table

    def show_drive(self, drive_id):
        storage_service_collection = \
            self.client.get_storage_service_collection()

        for storage_inst in storage_service_collection.get_members():
            if drive_id in storage_inst.drives.members_identities:
                storage = storage_inst
                break

        drive = storage.drives.get_member(drive_id)

        return utils.extract_attr(drive)

    def list_storage_pool(self, storage_uri):
        storage = self.client.get_storage_service(storage_uri)

        storage_pool_collection = storage.storage_pools.get_members()
        storages = [utils.extract_attr(storage_pool)
                    for storage_pool in storage_pool_collection]
        storage_pool_info_table = utils.print_dict(
            storages, ["Identity", "Name", "Description"])
        return storage_pool_info_table

    def show_storage_pool(self, storage_pool_id):
        storage = self.client.get_storage_service(
            self._extract_storage_service_uri(storage_pool_id))
        storage_pool = storage.storage_pools.get_member(storage_pool_id)

        return utils.extract_attr(storage_pool)
