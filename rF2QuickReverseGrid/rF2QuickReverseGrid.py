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
Main program
"""

import time
import random
import psutil

from pyRfactor2SharedMemory.sharedMemoryAPI import SimInfoAPI, Cbytestring2Python
from rF2QuickReverseGrid.setting import Setting

VERSION = "0.3.1"


def display_welcome():
    """Display welcome screen"""
    ver_length = len(VERSION) + 1
    text_space = " " * int((68 - ver_length) / 2)
    if ver_length % 2 == 0:
        text_ver = f"v{VERSION}"
    else:
        text_ver = f"v{VERSION} "

    print("")
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃                                                                    ┃")
    print("┃                 rF2 Quick Reverse Grid by S.Victor                 ┃")
    print(f"┃{text_space}{text_ver}{text_space}┃")
    print("┃                                                                    ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")


def display_setting(app_pid, preset_name, cfg):
    """Display current setting"""
    if cfg.base["full_random_grid"]:
        mode_text1 = "Fully Randomized Grid:           ON"
    else:
        mode_text1 = "Fully Randomized Grid:           OFF"

    if cfg.base["random_reverse_range"]:
        mode_text2 = "Randomized Reverse Range:        ON"
    else:
        mode_text2 = "Randomized Reverse Range:        OFF"

    if cfg.base["weight_penalty"]:
        mode_text3 = "Weight Penalty:                  ON"
    else:
        mode_text3 = "Weight Penalty:                  OFF"

    if cfg.base['server_mode']:
        mode_text4 = f"Mode:                            Dedicated Server (PID: {app_pid})"
    else:
        mode_text4 = f"Mode:                            Local Client"

    print("")
    print(f" Loaded Preset:                   {preset_name.upper()}")
    print(f" Executable:                      {cfg.base['rf2_executable_name']}")
    print(f" {mode_text4}")
    print("")
    print(f" {mode_text1}")
    print(f" {mode_text2}")
    print(f" {mode_text3}")
    print(f" Minimum Players to Reverse:      {cfg.base['min_reverse_limit']}")
    print(f" Maximum Players to Reverse:      {cfg.base['max_reverse_limit']}")

    if cfg.base["weight_penalty"]:
        print(f" Penalty Mass(kg): {cfg.base['penalty_mass_list']}")

    print("")


def set_batch_path(exe_name):
    """Set batch file output path"""
    for app in psutil.process_iter(["name", "pid"]):
        if app.info["name"] == exe_name:
            app_pid = app.info["pid"]
            app_path = app.exe()
            log_path = app_path.replace(f"Bin64\\{exe_name}", "UserData\\Log\\Results\\")
            rf2_status = 1
            break
        else:
            app_pid = ""
            log_path = None
            rf2_status = 0
    return app_pid, log_path, rf2_status


def auto_close_msg():
    print(" rF2QuickReverseGrid will be closed in 3", end="\r")
    time.sleep(1)
    print(" rF2QuickReverseGrid will be closed in 2", end="\r")
    time.sleep(1)
    print(" rF2QuickReverseGrid will be closed in 1", end="\r")
    time.sleep(1)
    print("")


def save_batch_file(listname, filepath, filename):
    batch_file = open(f"{filepath}{filename}.ini", "w")

    for index in listname:
        batch_file.write(index + "\n")

    batch_file.close()


def run():
    # Status toggle
    preset_status = 0

    # Start loop
    while True:

        if not preset_status:
            # Display welcome screen
            display_welcome()

            # Load configuration
            print("Press [Enter] to use Default preset, or Type a preset name:")
            race_preset = input("")

            if race_preset == "":
                print(" Preset name not set. Default.json will be used.")
                race_preset = "default"
                time.sleep(0.5)

            cfg = Setting(race_preset)
            preset_status = 1

            # Load RF2 info
            app_pid, log_path, rf2_status = set_batch_path(cfg.base['rf2_executable_name'])

            if not rf2_status:
                print("\n rFactor 2 is Not Running.\n")
                # Choices
                wait_app = input(" > Please start rFactor 2 then Press [Enter] to contiune\n"
                                 " > or Press [Q] then [Enter] to Quit\n"
                                 )
                if wait_app.upper() == "":
                    preset_status = 0
                else:
                    break

            # Load Shared Memory API
            if rf2_status:
                if cfg.base['server_mode']:
                    info = SimInfoAPI(app_pid)
                else:
                    info = SimInfoAPI("")


        if rf2_status:

            # Display current setting
            display_setting(app_pid, race_preset, cfg)

            # Choices
            exit_app = input(" > Press [Enter] to Generate Grid\n"
                             " > Press [L] then [Enter] to Load Preset\n"
                             " > Press [Q] then [Enter] to Quit\n"
                             )

            if exit_app.upper() == "L":
                preset_status = 0
            elif exit_app.upper() != "":
                break

            print("\n\n\n\n")

            # Create empty list
            unsorted_grid = []
            reverse_grid = []
            driver_list = []
            normal_grid = []
            batch_grid_reverse = []
            batch_grid_random = []

            # Create driver position list from current race session
            for index in range(max(info.Rf2Scor.mScoringInfo.mNumVehicles, 0)):
                place = info.Rf2Scor.mVehicles[index].mPlace
                driver = Cbytestring2Python(info.Rf2Scor.mVehicles[index].mDriverName)
                unsorted_grid.append((place,     # overall position
                                      driver,    # player name
                                      ))
                driver_list.append(driver)

            sorted_grid = sorted(unsorted_grid)
            total_players = len(sorted_grid)

            # Set Reverse Grid Limit
            if cfg.base["random_reverse_range"]:
                reverse_limit = random.randint(int(cfg.base["min_reverse_limit"]), int(cfg.base["max_reverse_limit"]))
            else:
                reverse_limit = int(cfg.base["max_reverse_limit"])

            # Create penalty mass list if enabled
            if cfg.base["weight_penalty"]:
                penalty_mass = cfg.base["penalty_mass_list"]

                for index in range(total_players):
                    if index < len(penalty_mass):
                        batch_grid_reverse.append((f"/setmass {penalty_mass[index]} {sorted_grid[index][1]}"))

            # Create reverse grid list
            for index in range(total_players):
                if index < reverse_limit:
                    reverse_grid.append((sorted_grid[index][0], sorted_grid[index][1]))
                else:
                    normal_grid.append((sorted_grid[index][0], sorted_grid[index][1]))

            reverse_players = len(reverse_grid)
            sorted_reverse_grid = sorted(reverse_grid, reverse=True)

            # Create final combined grid list
            final_grid = sorted_reverse_grid + normal_grid

            for index in range(len(final_grid)):
                # Create reverse grid
                if index < reverse_players:
                    batch_grid_reverse.append((f"/editgrid {reverse_players + 1 - final_grid[index][0]} {final_grid[index][1]}"))
                # Create normal grid
                else:
                    batch_grid_reverse.append((f"/editgrid {final_grid[index][0]} {final_grid[index][1]}"))

            # Create random grid list
            if cfg.base["full_random_grid"]:
                random_reverse_grid = random.sample(driver_list, total_players)

                for index in range(total_players):
                    batch_grid_random.append((f"/editgrid {index + 1} {random_reverse_grid[index]}"))

            # Save grid batch file
            try:
                save_batch_file(batch_grid_reverse, log_path, "reverse_grid")
                time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print("")
                print(f"Successfully updated grid batch file at {time_stamp}")
                print(f"{log_path}reverse_grid.ini")
                if cfg.base["full_random_grid"]:
                    save_batch_file(batch_grid_random, log_path, "random_grid")
                    print(f"{log_path}random_grid.ini")
                print("")
                print(f"Current grid is top {reverse_limit} drivers reversed.")
                print("")
                print("Copy & Paste below command during Warmup-Session to apply grid:")
                print("/batch reverse_grid.ini")
                if cfg.base["full_random_grid"]:
                    print("/batch random_grid.ini")
                print("")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

            except:
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print("Failed To Save Batch File, Something Wrong!")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


if __name__ == "__main__":
    run()
