# -*- coding: utf-8 -*-

import os, sys

def change_file_name():
    file_path = sys.argv[1]
    add_letter = sys.argv[2]
    all_file = os.listdir(file_path)
    for one_file in all_file:
        new_file_name = add_letter + one_file
        original_file_path = os.path.join(file_path,one_file)
        new_file_path = os.path.join(file_path, new_file_name)
        c = os.path.splitext(original_file_path)
        if c[1] == '.mp3':
            os.rename(original_file_path,new_file_path)

change_file_name()