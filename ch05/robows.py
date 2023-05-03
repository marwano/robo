#!/usr/bin/env python3
from datetime import datetime
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
import json
import motor

class MainHandler(RequestHandler):
    def get(self, name):
        stamp = datetime.now().isoformat()
        self.write(dict(stamp=stamp))

    def post(self, name):
        args = json.loads(self.request.body or '{}')
        func = getattr(motor, name)
        func(**args)
        self.write(dict(status='success'))

app = Application([('/(.*)', MainHandler)])
app.listen(8888)
IOLoop.current().start()
