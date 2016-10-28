# -*- coding: utf-8 -*-
#!/usr/bin/env python
__author__ = 'Elf'



import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado
import  os

from tornado.options import options, define

from api_virastar.url.main_url import url_pattern
from conf import Config

config = Config()

define("port", default=config.web['port'], help="run on the given port", type=int)


class WebSystemApplication(tornado.web.Application):
    def __init__(self):
        handlers = url_pattern
        settings = dict(
            debug=True,
            autoreload=True,
            template_path = os.path.join(os.path.dirname(__file__), "api_virastar/template"),
            static_path = os.path.join(os.path.dirname(__file__),"api_virastar/static")
        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(WebSystemApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
