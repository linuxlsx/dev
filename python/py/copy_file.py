import os
import shutil
import sys
from os.path import join, exists

def copy_file(src, dest):
    print dest
    for path, dirs, files in os.walk(src, topdown=True):
        if len(dirs) > 0:
            for di in dirs:
                copy_file(join(path, di), join(dest, di))
                dirs.remove(di)
        if not exists(dest):
            os.makedirs(dest)
        for fi in files:
            shutil.copy(join(path, fi), dest)

if __name__ == "__main__":
    if len(sys.argv) < 3 :
        print "you should specified the src and dest diretory!!"
        exit(0)
    copy_file(sys.argv[1], sys.argv[2])