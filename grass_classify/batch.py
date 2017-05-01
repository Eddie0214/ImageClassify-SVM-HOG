#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from os import listdir
from os.path import isfile, join

source_path = '/home/lbp/disk_data/out/rename'
out_path = '/home/lbp/disk_data/out'

onlyfiles = [f for f in listdir(source_path) if isfile(join(source_path, f))]

for file_name in onlyfiles:
    file_new = file_name.replace('.mp4.mp4', '.mp4')
    source_file = join(source_path, file_name)
    out_file = join(out_path, file_new)
    comm = 'mv {0} {1}'.format(source_file, out_file)
    print comm
    os.system(comm)