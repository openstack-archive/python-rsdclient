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

from rsd_lib.resources.v2_1.node import constants as node_cons

from rsdclient.common import base
from rsdclient.common import utils


class NodeManager(base.Manager):
    # resource_class = Node
    _resource_name = 'nodes'

    def __init__(self, *args, **kwargs):
        super(NodeManager, self).__init__(*args, **kwargs)
        self.nodes_path = self.client._nodes_path

    def compose(self, name=None, description=None, processor_req=None,
                memory_req=None, remote_drive_req=None, local_drive_req=None,
                ethernet_interface_req=None, security_req=None):
        node_uri = self.client.get_node_collection().compose_node(
            name=name, description=description, processor_req=processor_req,
            memory_req=memory_req, remote_drive_req=remote_drive_req,
            local_drive_req=local_drive_req,
            ethernet_interface_req=ethernet_interface_req,
            security_req=security_req)

        # Assume most of user will assemble node after composition, so assemble
        # node automatically here
        node = self.client.get_node(node_uri)
        node.assemble_node()

        return node_uri

    def delete(self, node_uri):
        self.client.get_node(node_uri).delete_node()

    def show(self, node_uri):
        node = self.client.get_node(node_uri)
        node_info = utils.extract_attr(node)

        node_info['allowed_attach_endpoints'] = \
            list(node.get_allowed_attach_endpoints())
        node_info['allowed_detach_endpoints'] = \
            list(node.get_allowed_detach_endpoints())
        node_info['allowed_boot_source'] = \
            list(node.get_allowed_node_boot_source_values())
        node_info['allowed_reset_node_values'] = \
            list(node.get_allowed_reset_node_values())

        return node_info

    def list(self):
        node_collection = self.client.get_node_collection()
        nodes = [utils.extract_attr(self.client.get_node(node_uri))
                 for node_uri in node_collection.members_identities]
        node_info_table = utils.print_dict(
            nodes, ["Identity", "Name", "UUID", "Description"])
        return node_info_table

    def attach(self, node_uri, endpoint=None, protocol=None):
        node = self.client.get_node(node_uri)
        node.attach_endpoint(endpoint, protocol)

    def detach(self, node_uri, endpoint):
        node = self.client.get_node(node_uri)
        node.detach_endpoint(endpoint)

    def reset(self, node_uri, action):
        node = self.client.get_node(node_uri)
        node.reset_node(action)

    def set_boot_source(self, node_uri, target, enabled=None, mode=None):
        if not enabled:
            enabled = node_cons.BOOT_SOURCE_ENABLED_ONCE

        node = self.client.get_node(node_uri)
        node.set_node_boot_source(target, enabled, mode)
