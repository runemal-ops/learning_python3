#!/usr/bin/env python
import subprocess, os
from multiprocessing import Pool
import re

src = "/home/student-02-06020a2dba22/data/prod"

def  sync_dir(directory):
	src = directory
    dest = re.sub("(/prod)",r"\1"+"_backup", src)
    print("Moving Data from {} to {}".format(src, dest))
    subprocess.call(["rsync", "-arq", src, dest])


if __name__ == "__main__":
    dir_list = []
    for root, dirs, files in os.walk(src, topdown=False):
        for name in dirs:
            dir_list.append(os.path.join(root, name))
    p = Pool(len(dir_list))
    p.map(sync_dir, dir_list)