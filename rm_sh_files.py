#!/usr/bin/env bash
import glob
import os

current_dir = "."
sh_files = "*.sh"
file_paths = glob.glob(os.path.join(current_dir, sh_files))
for file_path in file_paths:
    os.remove(file_path)
