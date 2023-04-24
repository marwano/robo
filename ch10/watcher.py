#!/usr/bin/env python3
import sys
import time
from os.path import getmtime

class FileWatcher:
    def __init__(self, path):
        self.path = path
        self.last_mtime = None

    def has_changed(self):
        mtime = getmtime(self.path)
        last_mtime = self.last_mtime
        self.last_mtime = mtime
        return (mtime != last_mtime)

def main():
    path = sys.argv[1]
    print('path:', path)
    watcher = FileWatcher(path)
    for i in range(10):
        print(i, watcher.has_changed())
        time.sleep(1 / 60)

if __name__ == "__main__":
    main()
