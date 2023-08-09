import os
import subprocess

import tornado.web
from tornado import define, options

base_path = "/usr/local/test/"
# base_path = "/"


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        path_list = [base_path + path for path in os.listdir(base_path)]
        self.render("index.html", path_list=path_list)

    def post(self, *args, **kwargs):
        new_path = self.get_argument("cmd").split(" ")[0]
        if os.path.isdir(new_path) and base_path in new_path:
            new_path = new_path + "/"
            path_list = [new_path + path for path in os.listdir(new_path)]
        else:
            path_list = [base_path + path for path in os.listdir(base_path)]
            self.render("index.html", path_list=path_list)
        option_html = ""
        for path in path_list:
            option_html += "<option>{}</option>".format(path)
        self.write(option_html)


class ExecuteHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        cmd = self.get_argument("cmd")
        if ".sh" or "ctsh" in cmd:
            status, output = subprocess.getstatusoutput("sh " + cmd)
            self.write(output)
        else:
            self.write("不是shell脚本")


if __name__ == "__main__":
    define("port", default=19999, type=int)
    tornado.options.parse_command_line()

    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "debug": True,
    }  # 配置静态文件路径

    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/execute", ExecuteHandler),
        ],
        **settings,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
