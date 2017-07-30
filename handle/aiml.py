# -*- coding: utf-8 -*-
import tornado.escape
import tornado.web

from BaseHTTPServer import HTTPServer

import config

class Alice(tornado.web.RequestHandler):
    def get(self):
        req = self.get_argument('req', 'default')
        if req and req != 'default':
            self.write(config.alice.respond(req))

    def post(self):
        self.write('Please use POST method !')
