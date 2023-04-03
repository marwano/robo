#!/usr/bin/env python3
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.log import enable_pretty_logging
from datetime import datetime
from os.path import dirname
import os
import motor

DEBUG = bool(os.environ.get('ROBO_DEBUG'))
TEMPLATE_PATH = (dirname(__file__) + '/templates')

class MainHandler(RequestHandler):
    def get(self, name):
        stamp = datetime.now().isoformat()
        self.render('forward.html', stamp=stamp)

    def post(self, name):
        if name == 'forward':
            motor.forward()
        if name == 'backward':
            motor.backward()
        self.redirect('/')

enable_pretty_logging()
settings = dict(debug=DEBUG, template_path=TEMPLATE_PATH)
app = Application([('/([a-z_]*)', MainHandler)], **settings)
app.listen(8888)
IOLoop.current().start()
