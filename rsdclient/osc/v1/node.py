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

from osc_lib.command import command


class ComposeNode(command.Command):
    _description = "Compose a Node"

    def get_parser(self, prog_name):
        parser = super(ComposeNode, self).get_parser(prog_name)
        # NOTE: All arguments are positional and, if not provided
        # with a default, required.
        parser.add_argument('--name',
                            dest='name',
                            required=True,
                            metavar='<name>',
                            help='Name of the composed node.')
        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        args = {
            'Name': parsed_args.name
        }
        rsd_client.node.compose(args)
        print("Request to compose node %s was accepted"
              % parsed_args.name)


class DeleteNode(command.Command):
    _description = "Delete a Node"

    def get_parser(self, prog_name):
        parser = super(DeleteNode, self).get_parser(prog_name)
        parser.add_argument(
            'node',
            nargs='+',
            metavar='<node>',
            help='ID of the node(s) to delete.')

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)", parsed_args)
        rsd_client = self.app.client_manager.rsd
        for node in parsed_args.node:
            rsd_client.node.delete(node)
            print("Node {0} has been deleted.".format(node))
