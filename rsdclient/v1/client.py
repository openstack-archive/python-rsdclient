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

import rsd_lib

from rsdclient.v1 import fabric
from rsdclient.v1 import node
from rsdclient.v1 import storage_service


class Client(object):

    def __init__(self, base_url, username, password, verify=True):
        """A client class to control RSD pod manager

        :param base_url: The base URL to RSD pod manager.
        :param username: User account with admin access privilege
        :param password: User account password
        :param verify: Either a boolean value, a path to a CA_BUNDLE
            file or directory with certificates of trusted CAs. If set to
            True it will verify the host certificates; if False it will
            ignore verifying the SSL certificate; if it's a path the driver
            will use the specified certificate or one of the certificates
            in the directory. Defaults to True.
        """

        self.client = rsd_lib.RSDLib(base_url, username, password,
                                     verify=verify).factory()
        self.node = node.NodeManager(self.client)
        self.storage_service = \
            storage_service.StorageServiceManager(self.client)
        self.fabric = fabric.FabricManager(self.client)
