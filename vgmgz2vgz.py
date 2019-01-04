#!/usr/bin/env python3
import os
from common import is_vgm_gz, convert_to_vgz

directory = os.getcwd()
os.chdir(directory)  # todo: allow directory argument

for file in os.listdir(directory):
    filepath = os.path.join(directory, file)
    if is_vgm_gz(filepath):
        convert_to_vgz(filepath)
