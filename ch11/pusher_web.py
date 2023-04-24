#!/usr/bin/env python3
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.log import enable_pretty_logging
from os.path import dirname
import os
from pusher_qr import get_items, push_item

SETTINGS = dict(
    debug=bool(os.environ.get('ROBO_DEBUG')),
    template_path=dirname(__file__) + '/templates',
    static_path=dirname(__file__) + '/static',
)

class MainHandler(RequestHandler):
    def get(self, name):
        name = name or 'index'
        self.render(f'{name}.html', items=get_items())

    def post(self, code):
        push_item(code)
        self.redirect('items')

enable_pretty_logging()
app = Application([('/([a-z_]*)', MainHandler)], **SETTINGS)
app.listen(8888)
IOLoop.current().start()
