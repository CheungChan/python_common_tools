# -*- coding: utf-8 -*-
__author__ = "陈章"
__date__ = "2019-06-25 15:25"

import os
import subprocess
import sys
import time


def file_filter(name):
    return (not name.startswith(".")) and (not name.endswith(".swp"))


def file_times(path):
    for file in filter(file_filter, os.listdir(path)):
        yield os.stat(file).st_mtime


def print_stdout(process):
    stdout = process.stdout
    if stdout != None:
        print(stdout)


def main():
    # The path to watch
    watch_path = sys.argv[1]
    # We concatenate all of the arguments together, and treat that as the command to run
    command = " ".join(sys.argv[2:])

    print("path = {watch_path}".format(watch_path=watch_path))
    print("command = {command}".format(command=command))

    # How often we check the filesystem for changes (in seconds)
    wait = 1

    # The process to autoreload
    process = subprocess.Popen(command, shell=True)

    # The current maximum file modified time under the watched directory

    last_mtime = max(file_times(watch_path))
    while True:
        max_mtime = max(file_times(watch_path))
        print_stdout(process)
        if max_mtime > last_mtime:
            last_mtime = max_mtime
            print("Restarting process, command: {}".format(command))
            process.kill()
            process = subprocess.Popen(command, shell=True)
        time.sleep(wait)


if __name__ == "__main__":
    main()
