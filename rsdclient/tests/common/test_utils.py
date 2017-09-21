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

import testtools

from rsdclient.common import utils
from rsdclient.tests.common import fakes


class UtilsTest(testtools.TestCase):

    def test_extract_attr(self):
        fake_node = fakes.FakeNode()
        result = utils.extract_attr(fake_node)
        expected = fakes.FAKE_NODE_PYTHON_DICT
        self.assertEqual(result, expected)

    def test_str2boolean(self):
        self.assertEqual(utils.str2boolean("True"), True)
        self.assertEqual(utils.str2boolean("true"), True)
        self.assertEqual(utils.str2boolean("False"), False)
        self.assertEqual(utils.str2boolean("false"), False)
        self.assertEqual(utils.str2boolean("fake string"), "fake string")
        self.assertEqual(utils.str2boolean(""), "")
