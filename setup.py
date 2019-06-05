from cx_Freeze import setup, Executable
import os.path
import sys
import gooey
import wx

# Dependencies are automatically detected, but it might need
# fine tuning.

# Build using python setup.py build

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
# os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
# os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

# added_files = ['data_files/',
#                os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
#                os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
#                ]

buildOptions = dict(includes=["gooey", "wx"], excludes=[], include_files=[], build_exe='PDF Merge')

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('merge_folder.py', base=base) # icon='data_files/python_icon.ico')
]

setup(name='PDF Merge',
      version='0.1',
      description='Merge all PDFs in a folder',
      options=dict(build_exe=buildOptions),
      executables=executables)
