# rF2QuickReverseGrid

rF2QuickReverseGrid is an open-source grid batch tool for rF2.


## Feature
- Fast & easy reverse grid control helps reduce workload for server admin.
- Supports local client and dedicated server. 
- Supports user-defined configuration preset, which can be configured and switched easily.
- Supports reverse grid, randomized reverse range, full randomized grid, predefined weight penalty list.


## Requirements
rF2QuickReverseGrid requires The Iron Wolf’s rF2 Shared Memory Map Plugin, download it from here:  
https://forum.studio-397.com/index.php?threads/rf2-shared-memory-tools-for-developers.54282/

The plugin file `rFactor2SharedMemoryMapPlugin64.dll` should be placed in `rFactor 2\Bin64\Plugins` folder. This plugin also comes with some of the popular rF2 Apps, check `rFactor 2\Bin64\Plugins` folder first to see if it was installed already.


## Usage
1. Make sure The Iron Wolf’s `rF2 Shared Memory Map Plugin` is installed.

2. Download latest rF2QuickReverseGrid version from [Releases](https://github.com/s-victor/rF2QuickReverseGrid/releases) page, extract to a separated folder.

3. Launch `rFactor 2`.

4. Run `rF2QuickReverseGrid.exe`.

    *Important Note: rF2QuickReverseGrid requires `rFactor 2` in running to generate grid batch file.*

5. Type a preset name, then this preset will be loaded (or created if not exists). User can configure this preset by editing JSON file. See Configuration Guide for details.

6. Join a Multiplayer session as server admin, and wait race to finish.

7. Once all drivers has crossed finish line, Alt-tab back to rF2QuickReverseGrid window, and hit `Enter` key. A new grid batch file will be generated right way with text notification on screen.
    
    *Important Note: User must hit `Enter` key before race session has ended (ex. loading into next track), otherwise real-time driver standing info will be lost. Server Admin may want to extend `Delay After Race` period in game's setting file.*

8. Restart warmup session.

9. Copy & paste `/batch reverse_grid.ini` into chat box and hit `Enter` to apply grid.

    *Note: For multi-round race, just repeat step 7 to 9.*


## Configuration
rF2QuickReverseGrid supports user-defined configuration preset. Each preset file will be created or loaded after user entered a preset name in APP, and can be configured by editing `.json` file with text editor. If no preset name is set, `Default.json` preset will be used instead.

See [Configuration Guide](./docs/configuration.md) for details.


## Run from source

### Dependencies:
* [Python](https://www.python.org/) 3.8 or higher
* pyRfactor2SharedMemory
    * psutil (sub-dependency)


### Steps:
1. Download source code from [Releases](https://github.com/s-victor/rF2QuickReverseGrid/releases) page; or click `Code` button at the top of repository and select `Download ZIP`. You can also use `Git` tool to clone this repository.

2. Download this forked version of pyRfactor2SharedMemory source code from:  
https://github.com/s-victor/pyRfactor2SharedMemory  
It includes a few required changes for rF2QuickReverseGrid.

3. Extract rF2QuickReverseGrid source code ZIP file. Then extract pyRfactor2SharedMemory ZIP file and put `pyRfactor2SharedMemory` folder in the root folder of rF2QuickReverseGrid.

4. Install additional dependencies by using command:  
`pip3 install psutil`  
Note: sub-dependencies should be auto-installed alongside related packages.

5. To start rF2QuickReverseGrid, type command from root folder:  
`python run.py`  
(rF2QuickReverseGrid is currently tested and worked with Python 3.8+)

Note: if using `Git` tool to clone this repository, run command with `--recursive` to also clone submodule, such as:  
`git clone --recursive https://github.com/s-victor/rF2QuickReverseGrid.git`


## Build executable
Executable file can be built with [py2exe](http://www.py2exe.org).

To install py2exe, run command:  
`pip3 install py2exe`

To build executable file, run command:  
`python build_py2exe.py py2exe`

After building completed, you can find executable file in `dist\rF2QuickReverseGrid` folder.


## Credits
### Author:
rF2QuickReverseGrid is created by Xiang (S.Victor), with helps from other contributors.

See [docs\contributors.md](./docs/contributors.md) file for full list of contributors.

### Special thanks to:  
zxd1997 & Sheepy1977 for technical advice & support.  
The Iron Wolf for [rF2 Shared Memory Map Plugin](https://github.com/TheIronWolfModding/rF2SharedMemoryMapPlugin).  
Tony Whitley for [pyRfactor2SharedMemory](https://github.com/TonyWhitley/pyRfactor2SharedMemory) Library.  


## License

rF2QuickReverseGrid is licensed under the GNU General Public License v3.0 or later. See [LICENSE.txt](./LICENSE.txt) for full text.

Licenses and notices file for third-party software are located in `docs\licenses` folder, see [THIRDPARTYNOTICES.txt](./docs/licenses/THIRDPARTYNOTICES.txt) file for details.
