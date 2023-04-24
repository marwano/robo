#!/usr/bin/env python3
import os
import asyncio
import tornado.web
from watcher import FileWatcher

IMG_PATH = os.environ['XDG_RUNTIME_DIR'] + '/robo_stream.jpg'
POLL_DELAY = 1 / 60
CONTENT_TYPE = 'multipart/x-mixed-replace;boundary=image-boundary'
BOUNDARY = b'--image-boundary\r\n'
JPEG_HEADER = b'Content-Type: image/jpeg\r\n\r\n'

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        self.set_header('Content-Type', CONTENT_TYPE)
        watcher = FileWatcher(IMG_PATH)
        while True:
            if watcher.has_changed():
                img_bytes = open(IMG_PATH, 'rb').read()
                self.write(BOUNDARY + JPEG_HEADER + img_bytes)
                self.flush()
            await asyncio.sleep(POLL_DELAY)

async def main():
    app = tornado.web.Application([('/', MainHandler)])
    app.listen(9000)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()

asyncio.run(main())
