import os
import signal
import time
from subprocess import PIPE

import ldap
import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado import Subprocess, define, gen, options

base_path = "/usr/local/test/"
base_log_path = "/usr/local/test/"
host_ip = "10.10.20.165"

Subprocess(
    ["cd {} && python -m SimpleHTTPServer 19998".format(base_log_path)],
    stdout=PIPE,
    stderr=PIPE,
    shell=True,
)


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_cookie("username")


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        if username and password:
            oa_name = login_ldap(username, password)
            if oa_name:
                self.set_cookie("username", username)
                self.redirect("/")
            else:
                message = "用户名或密码不正确"
                self.render("fail.html", message=message)
        else:
            message = "用户名或密码不能为空"
            self.render("fail.html", message=message)


class LogoutHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.clear_cookie("username")
        self.redirect("/login")


class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        path_list = [base_path + path for path in os.listdir(base_path)]
        username = self.get_cookie("username")
        self.render(
            "index.html", username=username, path_list=path_list, host_ip=host_ip
        )

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        new_path = self.get_argument("cmd").split(" ")[0]
        if os.path.isdir(new_path) and base_path in new_path:
            new_path = new_path + "/"
            path_list = [new_path + path for path in os.listdir(new_path)]
        else:
            path_list = [base_path + path for path in os.listdir(base_path)]
        option_html = ""
        for path in path_list:
            option_html += "<option>{}</option>".format(path)
        self.write(option_html)


class ExecuteHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self):
        cmd = self.get_argument("cmd")
        if cmd:
            if os.path.isdir(cmd) and base_path in cmd:
                dt = time.strftime("[ %Y-%m-%d %H:%M:%S ] ")
                file_name = "{}.log".format(self.get_cookie("username"))
                with open(file_name, "ab") as f:
                    f.write(dt + "svn update " + cmd + "\n")
                process = yield self.run_command("svn update " + cmd)
                out, err = process.stdout.read(), process.stderr.read()
                if err:
                    message = err
                else:
                    message = out
            else:
                message = "不是目录或路径不正确"
        else:
            message = "不能为空"
        self.write({"message": message.replace("\n", "<br>")})

    @tornado.web.authenticated
    @gen.coroutine
    def post(self):
        cmd = self.get_argument("cmd")
        pid = None
        if cmd:
            apath = cmd.split(" ")[0]
            if base_path in apath and os.path.exists(apath):
                if ".sh" in cmd or ".ctsh" in cmd:
                    dt = time.strftime("[ %Y-%m-%d %H:%M:%S ] ")
                    file_name = "{}.log".format(self.get_cookie("username"))
                    with open(file_name, "ab") as f:
                        f.write(dt + cmd + "\n")
                    process = yield self.run_command("sh " + cmd)
                    out, err = process.stdout.read(), process.stderr.read()
                    # pid = process.pid
                    if err:
                        message = err
                    else:
                        message = out
                else:
                    message = "不是shell脚本"
            else:
                message = "路径不正确"
        else:
            message = "不能为空"
        self.write({"message": message.replace("\n", "<br>"), "pid": pid})

    @tornado.web.authenticated
    @gen.coroutine
    def run_command(self, command):
        process = Subprocess([command], stdout=PIPE, stderr=PIPE, shell=True)
        yield process.wait_for_exit(
            raise_error=False
        )  # This waits without blocking the event loop.
        # out, err = process.stdout.read(), process.stderr.read()
        # Do whatever you do with out and err
        raise tornado.gen.Return(process)

    @tornado.web.authenticated
    def kill(self, pid):
        os.kill(pid, signal.SIGKILL)


class HistoryHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = self.get_cookie("username")
        file_name = "{}.log".format(username)
        if os.path.exists(file_name):
            with open(file_name) as f:
                lines = f.readlines()
                history = "\n".join(lines[-50:]).strip()
        else:
            history = "没有历史记录"
        self.render("history.html", history=history)


def login_ldap(username, password):
    try:
        # print("开始执行"
        # Server = "LDAP://tg.com.local"
        Server = "ldap://10.10.20.154:389"
        # baseDN = "dc=domainname,dc=com"
        baseDN = "dc=tg,dc=com,dc=local"
        # root_dn = cn=admin,dc=qijia,dc=com
        # root_pw = jiacom
        searchScope = ldap.SCOPE_SUBTREE
        # 设置过滤属性，这里只显示cn=test的信息
        searchFilter = "sAMAccountName=" + username
        # 为用户名加上域名
        username = "tg\\" + username
        # None表示搜索所有属性，['cn']表示只搜索cn属性
        retrieveAttributes = None
        conn = ldap.initialize(Server)
        # 非常重要
        conn.set_option(ldap.OPT_REFERRALS, 0)
        conn.protocol_version = ldap.VERSION3
        # 这里用户名是域账号的全名例如domain/name
        conn.simple_bind_s(username, password)
        # print 'ldap connect successfully'
        # 调用search方法返回结果id
        ldap_result_id = conn.search(
            baseDN, searchScope, searchFilter, retrieveAttributes
        )
        result_set = []
        while 1:
            result_type, result_data = conn.result(ldap_result_id, 0)
            if result_data == []:
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)
        Name, Attrs = result_set[0][0]
        if hasattr(Attrs, "has_key") and "name" in Attrs:
            # distinguishedName = Attrs['mail'][0]
            # print "Login Info for user : %s" % distinguishedName
            # print Attrs['mail'][0]
            # print Attrs['name'][0]
            # print Attrs['displayName'][0]
            # print Attrs['memberOf'][0]
            # print Attrs['sAMAccountName'][0]
            # print Attrs['title'][0]
            # print Attrs['department'][0]
            # return distinguishedName
            return Attrs["name"][0]
        else:
            print("in error")
            return None
    except ldap.LDAPError as e:
        print("out error")
        print(e)
        return None


if __name__ == "__main__":
    define("port", default=19999, type=int)
    tornado.options.parse_command_line()

    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        # "xsrf_cookies": True,
        "login_url": "/login",
        "debug": True,
    }  # 配置静态文件路径

    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/execute", ExecuteHandler),
            (r"/login", LoginHandler),
            (r"/logout", LogoutHandler),
            (r"/history", HistoryHandler),
        ],
        **settings,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
