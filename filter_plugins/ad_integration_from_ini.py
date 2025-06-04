# -*- coding: utf-8 -*-

# Copyright (c) 2023, Steffen Scheib <steffen@scheib.me>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

DOCUMENTATION = r"""
name: from_ini
short_description: Converts INI text input into a dictionary
version_added: 8.2.0
author: Steffen Scheib (@sscheib)
description:
  - Converts INI text input into a dictionary.
options:
  _input:
    description: A string containing an INI document.
    type: string
    required: true
"""

EXAMPLES = r"""
- name: Slurp an INI file
  ansible.builtin.slurp:
    src: /etc/rhsm/rhsm.conf
  register: rhsm_conf

- name: Display the INI file as dictionary
  ansible.builtin.debug:
    var: rhsm_conf.content | b64decode | community.general.from_ini

- name: Set a new dictionary fact with the contents of the INI file
  ansible.builtin.set_fact:
    rhsm_dict: >-
      {{
          rhsm_conf.content | b64decode | community.general.from_ini
      }}
"""

RETURN = r"""
_value:
  description: A dictionary representing the INI file.
  type: dictionary
"""

import sys

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six import string_types
from ansible.module_utils.six.moves import StringIO

if sys.version_info.major == 3:
    from ansible.module_utils.six.moves.configparser import ConfigParser
else:
    # use RawConfigParser because it uses interpolation=None
    from ConfigParser import RawConfigParser as ConfigParser


class IniParser(ConfigParser):
    """Implements a configparser which is able to return a dict"""

    def __init__(self):
        if sys.version_info.major == 2:
            ConfigParser.__init__(self)
        else:
            super().__init__(interpolation=None)
        self.optionxform = str

    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop("__name__", None)

        if self._defaults:
            d["DEFAULT"] = dict(self._defaults)

        return d

    def my_read_file(self, fp):
        if sys.version_info.major == 2:
            self.readfp(fp)
        else:
            self.read_file(fp)


def from_ini(obj):
    """Read the given string as INI file and return a dict"""

    if not isinstance(obj, string_types):
        raise AnsibleFilterError("from_ini requires a str, got %s" % type(obj))

    parser = IniParser()

    try:
        parser.my_read_file(StringIO(obj))
    except Exception as ex:
        raise AnsibleFilterError(
            "from_ini failed to parse given string: %s" % str(ex), orig_exc=ex
        )

    return parser.as_dict()


class FilterModule(object):
    """Query filter"""

    def filters(self):

        return {"ad_integration_from_ini": from_ini}
