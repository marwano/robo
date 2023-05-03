#!/usr/bin/env python3
from datetime import datetime
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

class MainHandler(RequestHandler):
    def get(self):
        stamp = datetime.now().isoformat()
        self.write(dict(stamp=stamp))

app = Application([('/', MainHandler)])
app.listen(8888)
IOLoop.current().start()
