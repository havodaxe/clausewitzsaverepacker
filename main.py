#!/usr/bin/env python3

from glob import glob
from os import path, mkdir
from sys import argv

output_not_empty = "{}/ not empty, back up or clear out contents"

print(argv)

output_dir = input("Output directory: ")

if(output_dir == ""):
    output_dir = "output"

if(not path.exists("{}/".format(output_dir))):
    mkdir("{}".format(output_dir))

if(len(glob("{}/*".format(output_dir))) != 0):
    raise RuntimeError(output_not_empty.format(output_dir))

