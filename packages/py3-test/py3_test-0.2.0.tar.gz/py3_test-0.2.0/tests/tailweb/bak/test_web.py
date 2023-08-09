import os

import tornado.web
from tornado import define, options


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self, *args, **kwargs):
        pass


if __name__ == "__main__":
    define("port", default=8000, type=int)
    tornado.options.parse_command_line()

    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "debug": True,
    }  # 配置静态文件路径

    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
        ],
        **settings,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
