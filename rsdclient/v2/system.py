#   Copyright 2019 Intel, Inc.
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


class SystemManager(base.Manager):
    _resource_name = 'systems'

    def __init__(self, *args, **kwargs):
        super(SystemManager, self).__init__(*args, **kwargs)
        self.systems_path = self.client._systems_path

    def list(self):
        system_collection = self.client.get_system_collection()
        systems = [utils.extract_attr(self.client.get_system(system_uri))
                   for system_uri in system_collection.members_identities]
        system_info_table = utils.print_dict(
            systems, ["Identity", "Name", "Description"])
        return system_info_table

    def show(self, system_uri):
        system = self.client.get_system(system_uri)
        system_dict = utils.extract_attr(system)
        return system_dict
