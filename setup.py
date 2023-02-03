import sys
from cx_Freeze import setup, Executable

# Define the main script
base = None
if sys.platform == "win32":
   base = "Win32GUI"

executables = [Executable("main.py", base=base, targetName = "LES Solver", icon="icon.ico")]

# Build the .exe file
setup(
   name = "LES Solver",
   options={"build_exe": {"packages": ["tkinter"], "include_files": ["icon.ico",]}},
   version = "1.0",
   description = "This app solves m x n LESystems",
   executables = executables
)