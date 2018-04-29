import sys
import cx_Freeze

executables = [cx_Freeze.Executable("main.py",base="Win32GUI",shortcutName="Universal Search",shortcutDir="DesktopFolder",icon="icon.ico",targetName="US.exe",)]

includefiles = ["settings", "icons"]


cx_Freeze.setup(
    name="CP Editor",
    version ="1.0",
    author="Shubham Shukla",
    options={"build_exe":{'include_files':includefiles}},
    description = "Notepad by Shubham Shukla",
    executables = executables
    )
