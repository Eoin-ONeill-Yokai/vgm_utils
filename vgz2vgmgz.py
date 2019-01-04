#!/usr/bin/env python3
import os
from common import is_vgz, convert_to_vgm_gz

directory = os.getcwd()
os.chdir(directory)  # todo: allow directory argument

for file in os.listdir(directory):
    filepath = os.path.join(directory, file)
    if is_vgz(filepath):
        convert_to_vgm_gz(filepath)
