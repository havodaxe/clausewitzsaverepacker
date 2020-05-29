#!/usr/bin/env python3

from glob import glob
from os import path, mkdir, utime
from sys import argv
from subprocess import run
from datetime import datetime

output_not_empty = "{}/ not empty, back up or clear out contents"

output_dir = input("Output directory: ")
#output_dir = ""

if(output_dir == ""):
    output_dir = "output"

if(not path.exists("{}/".format(output_dir))):
    mkdir("{}".format(output_dir))

if(len(glob("{}/*".format(output_dir))) != 0):
    raise RuntimeError(output_not_empty.format(output_dir))

save_paths = sorted(argv[1:], key=path.getmtime)

for save_path in save_paths:
    extract_path = "{}/{}".format(output_dir, save_path[:-4])
    mkdir(extract_path)
    run(["unzip", save_path, "-d", extract_path])
    timestamp = path.getmtime(save_path)
    with open("{}/time".format(extract_path), "wt") as timefile:
        timefile.write("{}\n".format(timestamp))
        timefile.write("{}\n".format(datetime.fromtimestamp(timestamp)))
    utime(extract_path, (timestamp, timestamp))
    # I think this has to be done after all the other things as they
    # edit the directory

