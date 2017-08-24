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

import os

from rsdclient.common import base
from rsdclient.common import utils


class StorageManager(base.Manager):
    _resource_name = 'storages'

    def __init__(self, *args, **kwargs):
        super(StorageManager, self).__init__(*args, **kwargs)
        self.storage_service_path = self.client._storage_service_path

    def _get_storage_service_uri(self, storage_service_id):
        return os.path.join(self.storage_service_path, storage_service_id)

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

    def show(self, storage_id):
        storage = self.client.get_storage_service(
            self._get_storage_service_uri(storage_id))
        storage_dict = utils.extract_attr(storage)

        # Append sub-items attributions
        storage_dict['remote_targets'] = [
            utils.extract_attr(item)
            for item in storage.remote_targets.get_members()]
        storage_dict['physical_drives'] = [
            utils.extract_attr(item)
            for item in storage.physical_drives.get_members()]
        storage_dict['logical_drives'] = [
            utils.extract_attr(item)
            for item in storage.logical_drives.get_members()]

        return storage_dict
