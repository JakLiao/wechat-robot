# -*- coding: utf-8 -*-
import os
import tornado.web

settings = {
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'template_path': os.path.join(os.path.dirname(__file__), 'view'),
            'login_url':'/',
            'session_timeout':3600,
            }

import aiml
cur_dir = os.getcwd()
print 'cur_dir:', cur_dir
os.chdir('./res/alice')
alice = aiml.Kernel()
alice.learn("startup.xml")
alice.respond('LOAD ALICE')
os.chdir(cur_dir)
print 'cur_dir:', os.getcwd()

from handle import *

handlers=[
        (r'/aiml', aiml.Alice),
        ]
