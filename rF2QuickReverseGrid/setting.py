#  rF2QuickReverseGrid is an open-source grid batch tool for rF2.
#  Copyright (C) 2022  Xiang
#
#  This file is part of rF2QuickReverseGrid.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
Setting
"""

import time
import json
import shutil


class Setting:
    """APP setting

    Call load() to load last saved setting before assigning changes.
    """
    setting_default = {
        "Base": {
            "rf2_executable_name": "rFactor2.exe",
            "server_mode": False,
            "full_random_grid": False,
            "random_reverse_range": False,
            "min_reverse_limit": 6,
            "max_reverse_limit": 10,
            "weight_penalty": False,
            "penalty_mass_list": [60,54,48,42,36,30,24,18,12,6],
        },
    }

    def __init__(self, preset_name):
        self.filename = f"{preset_name}.json"
        self.setting_user = {}
        self.load()

    def load(self):
        """Load & validate setting"""
        try:
            # Read JSON file
            with open(self.filename, "r", encoding="utf-8") as jsonfile:
                self.setting_user = json.load(jsonfile)

            # Verify setting
            verify_setting(self.setting_user, self.setting_default)

            # Save setting to JSON file
            self.save()
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.backup()
            self.restore()
            self.save()

        # Assign base setting
        self.base = self.setting_user["Base"]

    def save(self):
        """Save setting to file"""
        with open(self.filename, "w", encoding="utf-8") as jsonfile:
            json.dump(self.setting_user, jsonfile, indent=4)

    def restore(self):
        """Restore default setting"""
        self.setting_user = self.setting_default.copy()

    def backup(self):
        """Backup invalid file"""
        try:
            time_stamp = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
            shutil.copy(self.filename, f"config-backup {time_stamp}.json")
        except FileNotFoundError:
            pass


def check_invalid_key(target, origin, dict_user):
    """First step, check & remove invalid key from user list"""
    for _, key in enumerate(target):  # loop through user key list
        if key not in origin:  # check each user key in default list
            dict_user.pop(key)  # remove invalid key


def check_missing_key(target, origin, dict_user, dict_def):
    """Second step, adding missing default key to user list"""
    for _, key in enumerate(target):  # loop through default key list
        if key not in origin:  # check each default key in user list
            dict_user[key] = dict_def[key]  # add missing item to user


def check_key(dict_user, dict_def):
    """Create key-only check list, then validate key"""
    key_list_def = list(dict_def)
    key_list_user = list(dict_user)
    check_invalid_key(key_list_user, key_list_def, dict_user)
    check_missing_key(key_list_def, key_list_user, dict_user, dict_def)


def verify_setting(dict_user, dict_def):
    """Verify setting"""
    # Check top-level key
    check_key(dict_user, dict_def)
    # Check sub-level key
    for item in dict_user.keys():  # list each key lists
        check_key(dict_user[item], dict_def[item])
