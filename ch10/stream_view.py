#!/usr/bin/env python3
import os
import cv2
from watcher import FileWatcher

IMG_PATH = os.environ['XDG_RUNTIME_DIR'] + '/robo_stream.jpg'
ESC_KEY = 27

def main():
    watcher = FileWatcher(IMG_PATH)
    while cv2.waitKey(1) not in [ord('q'), ESC_KEY]:
        if watcher.has_changed():
            img = cv2.imread(IMG_PATH)
            cv2.imshow('preview', img)

main()
