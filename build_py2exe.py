"""
py2exe build script
"""
from distutils.core import setup
from glob import glob
import py2exe

from rF2QuickReverseGrid.rF2QuickReverseGrid import VERSION


app_setting = [{
    "script": "run.py",
    "dest_base": "rF2QuickReverseGrid",
    }
]

excludes = ["_ssl", "difflib", "email", "pdb", "venv", "http", "tkinter"]

data_files = [("", ["LICENSE.txt", "README.md"]),
              ("docs", ["docs/changelog.txt", "docs/configuration.md", "docs/contributors.md", "docs/features.md"]),
              ("docs/licenses", glob("docs/licenses/*")),
              ]

options = {
    "py2exe":{
        "dist_dir": "dist/rF2QuickReverseGrid",
        "excludes": excludes,
        "dll_excludes": ["libcrypto-1_1.dll"],
        "optimize": 2,
        "bundle_files": 2,
        "compressed": 1,
    }
}

setup(
    name = "rF2 Quick Reverse Grid",
    version = VERSION,
    description= "Open-source grid batching tool for rF2",
    author = "Xiang",
    console = app_setting,
    options = options,
    data_files = data_files,
    zipfile = "lib/library.zip",
)