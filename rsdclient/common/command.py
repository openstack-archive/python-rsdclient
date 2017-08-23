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

from cliff import _argparse

from osc_lib.command import command


class Command(command.Command):

    def get_parser(self, prog_name):
        parser = super(Command, self).get_parser(prog_name)
        parser.formatter_class = _SmartHelpFormatter

        return parser


class _SmartHelpFormatter(_argparse.HelpFormatter):
    """New smart argparse HelpFormatter

       Smart help formatter to output raw help message if it contains newline
       and heading whitespaces.
    """

    def _split_lines(self, text, width):
        lines = text.splitlines() if '\n' in text else [text]
        wrap_lines = []
        for each_line in lines:
            if each_line == '':
                # Handle newline case
                wrap_lines.append('')
            elif each_line.startswith(' '):
                # Handle heading whitespaces case
                spaces_width = len(each_line) - len(each_line.lstrip())
                lines = super(_SmartHelpFormatter, self)._split_lines(
                    each_line, width - spaces_width)
                wrap_lines.extend([' ' * spaces_width + line
                                   for line in lines])
            else:
                # Handle normal case
                wrap_lines.extend(
                    super(_SmartHelpFormatter, self)._split_lines(
                        each_line, width)
                )
        return wrap_lines
