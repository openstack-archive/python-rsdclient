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


class NodeManager(base.Manager):
    # resource_class = Node
    _resource_name = 'nodes'

    def __init__(self, *args, **kwargs):
        super(NodeManager, self).__init__(*args, **kwargs)
        self.nodes_path = self.client._nodes_path

    def _get_node_uri(self, node_id):
        return os.path.join(self.nodes_path, node_id)

    def compose(self, properites):
        # TODO(lin.yang): should return id of new composed node, like
        # 'redfish/v1/Nodes/1'
        return self.client.get_node_collection().compose_node(properites)

    def delete(self, node_id):
        self.client.get_node(self._get_node_uri(node_id)).delete_node()
