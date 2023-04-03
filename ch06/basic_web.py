#!/usr/bin/env python3
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.log import enable_pretty_logging
from datetime import datetime
from os.path import dirname
import os

DEBUG = bool(os.environ.get('ROBO_DEBUG'))
TEMPLATE_PATH = (dirname(__file__) + '/templates')

class MainHandler(RequestHandler):
    def get(self):
        stamp = datetime.now().isoformat()
        self.render('basic.html', stamp=stamp)

enable_pretty_logging()
settings = dict(debug=DEBUG, template_path=TEMPLATE_PATH)
app = Application([('/', MainHandler)], **settings)
app.listen(8888)
IOLoop.current().start()
