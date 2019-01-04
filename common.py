#!/usr/bin/env python3
""" vgmutils/common.py
Utilities meant for multiple python files are to be stored here. Common
functions, shared configurations, etc.
"""

import os
from pathlib import Path


def is_vgz(filepath):
    if os.path.isfile(filepath):
        if filepath.endswith('.vgz'):
            return True
    return False


def is_vgm_gz(filepath):
    if os.path.isfile(filepath):
        if filepath.endswith('.vgm.gz'):
            return True
    return False


def convert_to_vgm_gz(filepath):
    '''
    Converts file from ".vgz" to ".vgm.gz"
    filepath: filepath
    returns: success (bool)
    '''
    if is_vgz(filepath):
        current_path = Path(filepath)
        new_extension = ".vgm.gz"
        old_extension = current_path.suffix
        name_without_extension = current_path.stem

        current_path.rename(Path(current_path.parent,
                                 name_without_extension + new_extension))
        print(name_without_extension + old_extension + " >> "
              + name_without_extension + new_extension)

        return True
    else:
        return False


def convert_to_vgz(filepath):
    '''
    Converts file from ".vgm.gz" file to ".vgz"
    filepath: filepath (string)
    returns: success (bool)
    '''
    if is_vgm_gz(filepath):
        current_path = Path(filepath)

        new_extension = ".vgz"
        old_extension = (Path(current_path.parent,
                              current_path.stem).suffix
                         + current_path.suffix)
        name_without_extension = Path(current_path.parent,
                                      current_path.stem
                                      ).stem

        current_path.rename(Path(current_path.parent,
                                 name_without_extension + new_extension))

        print(name_without_extension + old_extension + " >> "
              + name_without_extension + new_extension)
        return True
    else:
        return False
