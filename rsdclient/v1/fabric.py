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


class FabricManager(base.Manager):
    _resource_name = 'fabrics'

    def __init__(self, *args, **kwargs):
        super(FabricManager, self).__init__(*args, **kwargs)
        self.fabrics_path = self.client._fabrics_path

    def _get_fabric_uri(self, fabric_id):
        return os.path.join(self.fabrics_path, fabric_id)

    def list(self):
        fabric_collection = self.client.get_fabric_collection()
        fabrics = [utils.extract_attr(self.client.get_fabric(fabric_uri))
                   for fabric_uri in fabric_collection.members_identities]
        fabric_info_table = utils.print_dict(
            fabrics, ["Identity", "Name", "Fabric_Type", "Description"])
        return fabric_info_table

    def show(self, fabric_id):
        fabric = self.client.get_fabric(self._get_fabric_uri(fabric_id))
        fabric_dict = utils.extract_attr(fabric)

        # Append sub-items attributions
        fabric_dict['endpoints'] = [
            utils.extract_attr(item)
            for item in fabric.endpoints.get_members()]
        fabric_dict['zones'] = [
            utils.extract_attr(item)
            for item in fabric.zones.get_members()]

        return fabric_dict
