# Copyright 2017 Intel, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import prettytable
import six


def extract_attr(redfish_obj):
    '''Extract all public attributes of python redfish object

    :param redfish_obj: python redfish object returned by rsd_lib
    :returns: python dict of that object
    '''

    if isinstance(redfish_obj, (int, six.string_types)):
        return redfish_obj
    if isinstance(redfish_obj, list):
        return [extract_attr(i) for i in redfish_obj]
    if isinstance(redfish_obj, dict):
        return {i: extract_attr(redfish_obj[i]) for i in redfish_obj}

    result = {}
    try:
        for key, value in vars(redfish_obj).items():
            # Skip all private attributes
            if key.startswith('_'):
                continue
            result[key] = extract_attr(value)
    except TypeError:
        return None

    return result


def print_dict(obj_list, field_names):
    pt = prettytable.PrettyTable(field_names=field_names)

    for element in obj_list:
        pt.add_row([element.get(i.lower(), None) for i in field_names])

    return pt


def str2boolean(string_obj):
    """Convert string 'True' and 'False' to corresponding boolean obj"""

    if string_obj.lower() == "true":
        return True
    elif string_obj.lower() == "false":
        return False
    else:
        return string_obj
