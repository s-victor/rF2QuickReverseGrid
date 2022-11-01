# Configuration Guide

rF2QuickReverseGrid supports user-defined configuration preset. Each preset file will be created or loaded after user entered a preset name in APP, and can be configured by editing `.json` file with text editor. If no preset name is set, `Default.json` preset will be used instead.

To make changes, editing `values` on the right side of colon.

Do not modify anything (keys) on the left side of colon, any changes to those keys will be reverted back to default setting by APP.

If APP fails to launch after editing `.json` file, check for typo error or invalid values.


## Backup file 
rF2QuickReverseGrid will automatically create a backup file with time stamp suffix if old setting file is invalid, and a new default `.json` will be generated.

A newer released version will auto-update old setting and add new setting. It is still recommended to manually create backup file before updating to new version.


## Editing Notes
If a value is surrounded by quotation marks, make sure not to remove those quotation marks, otherwise may cause error.

Any boolean type value (true or false) will only accept: `true`, which can be substituted with `1`. And `false`, which can be substituted with `0`. All words must be in `lowercase`, otherwise will have no effect.

If a number (default value) does not contain any decimal place, that means it only accepts `integer`. Make sure not to add any decimal place, otherwise error will occur.


## Base
    rf2_executable_name
Set rF2 executable filename. Default executable filename is for client, which should be `rFactor2.exe`. To use on server, change it to server executable filename, which should be `rFactor2 Dedicated.exe`, and then enable `server_mode`.

    server_mode
Set to `true` to enable server mode, which is required for reading real-time data from server. Server process PID will also be displayed on screen.

    full_random_grid
When set to `true`, an additional fully randomized grid will be saved as `random_grid.ini`.

    random_reverse_range
When set to `true`, the reverse-grid range will be randomly picked between `min_reverse_limit` and `max_reverse_limit`.

    min_reverse_limit
Set minimum reverse-grid range value. This value is only used if `random_reverse_range` is enabled.

    max_reverse_limit
Set maximum reverse-grid range value.

    weight_penalty
When set to `true`, weight penalty (as set in `penalty_mass_list`) will be added to players according to the final standing of last race.

    penalty_mass_list
Set a list of predefined weight penalty mass (in kilogram).
