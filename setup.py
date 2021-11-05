import  cx_Freeze
from cx_Freeze import Executable
import sys


# base
base=None
if sys.platform=='win32':
    base='win32GUI'

# exe
executables=[
    Executable(
        "StartUp.py",
        copyright="@2022 ENG-CJ",
        base=base,
        icon="icon_bitmap.ico",
        shortcut_name="Tic Tac",
        shortcut_dir='DesktopFolder'
    )
]

# setup
cx_Freeze.setup(
    name="Tic Tac",
    author='ENG-CJ',
    options={
        "build_exe":{"packages":["tkinter","PIL","webbrowser"],
                     "include_files":["tic.py","backgroudn.jpg","icon_bitmap.ico","info.png","tic tac toe.ico"]}
    },
    version='1.0.1',
    description="Tic Tac Toe Game | Play Your Free Time",
    executables=executables
)