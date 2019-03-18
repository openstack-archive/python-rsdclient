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


class FabricManager(base.Manager):
    _resource_name = 'fabrics'

    def __init__(self, *args, **kwargs):
        super(FabricManager, self).__init__(*args, **kwargs)
        self.fabrics_path = self.client._fabrics_path

    def _extract_fabric_uri(self, uri):
        if not uri.startswith(self.fabrics_path):
            return None

        return uri[:uri.find('/', len(self.fabrics_path) + 1)]

    def list(self):
        fabric_collection = self.client.get_fabric_collection()
        fabrics = [utils.extract_attr(self.client.get_fabric(fabric_uri))
                   for fabric_uri in fabric_collection.members_identities]
        fabric_info_table = utils.print_dict(
            fabrics, ["Identity", "Name", "Fabric_Type", "Description"])
        return fabric_info_table

    def show(self, fabric_uri):
        fabric = self.client.get_fabric(fabric_uri)
        fabric_dict = utils.extract_attr(fabric)

        # Append sub-items attributions
        fabric_dict['endpoints'] = [
            utils.extract_attr(item)
            for item in fabric.endpoints.get_members()]
        fabric_dict['zones'] = [
            utils.extract_attr(item)
            for item in fabric.zones.get_members()]

        return fabric_dict

    def list_endpoint(self, fabric_id):
        fabric = self.client.get_fabric(fabric_id)

        endpoint_collection = fabric.endpoints.get_members()
        endpoints = [utils.extract_attr(endpoint)
                     for endpoint in endpoint_collection]
        endpoint_info_table = utils.print_dict(
            endpoints, ["Identity", "Name", "Description"])
        return endpoint_info_table

    def show_endpoint(self, endpoint_id):
        fabric = self.client.get_fabric(
            self._extract_fabric_uri(endpoint_id))
        endpoint = fabric.endpoints.get_member(endpoint_id)

        return utils.extract_attr(endpoint)

    def create_endpoint(
            self, fabric_id, connected_entities, identifiers=None,
            protocol=None, pci_id=None, host_reservation_memory_bytes=None,
            ip_transport_details=None, links=None, oem=None):
        fabric = self.client.get_fabric(fabric_id)
        endpoint_collection = fabric.endpoints

        endpoint_uri = endpoint_collection.create_endpoint(
            connected_entities, identifiers=identifiers, protocol=protocol,
            pci_id=pci_id,
            host_reservation_memory_bytes=host_reservation_memory_bytes,
            ip_transport_details=ip_transport_details, links=links, oem=oem)

        return endpoint_uri
