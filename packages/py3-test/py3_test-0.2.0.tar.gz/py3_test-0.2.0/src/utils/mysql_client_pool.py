"""
Created on 2019/11/20
@author: lijc210@163.com
Desc: 功能描述。
"""

import pymysql
from dbutils.pooled_db import PooledDB
from pymysql.cursors import Cursor, DictCursor, SSCursor, SSDictCursor


class MySqlClientPool:
    def __init__(
        self,
        conn_dict,
        charset="utf8",
        cursorclass="dict",
        maxconnections=100,
        maxcached=10,
    ):
        self.host = conn_dict["host"]
        self.user = conn_dict["user"]
        self.passwd = conn_dict["passwd"]
        self.db = conn_dict["db"]
        self.charset = charset
        self.port = conn_dict["port"]
        self.cursorclass = cursorclass
        self.maxconnections = maxconnections
        self.maxcached = maxcached
        self.pool = self.pool()

    def pool(self):
        if self.cursorclass == "dict":
            cursorclass = DictCursor
        elif self.cursorclass == "ss_dict":
            cursorclass = SSDictCursor
        elif self.cursorclass == "ss_list":
            cursorclass = SSCursor
        else:
            cursorclass = Cursor

        pool = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=self.maxconnections,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=10,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            maxcached=self.maxcached,  # 链接池中最多闲置的链接，0和None不限制
            maxshared=100,
            # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
            setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
            ping=0,
            # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.passwd,
            database=self.db,
            charset=self.charset,
            cursorclass=cursorclass,
        )
        return pool

    def conn(self):
        conn = self.pool.connection()
        return conn

    def query(self, sql):
        conn = self.conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()  # 该连接返还给数据库连接池
        return results

    def query_cursor(self, sql):
        """
        游标查询，需要返回大数量时使用
        :param sql:
        :return:
        """
        conn = self.conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor

    def insert(self, sql):
        conn = self.conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()

    def update(self, sql):
        conn = self.conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()

    def execute(self, sql):
        conn = self.conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()

    def executemany(self, sql, sqlDataList):
        conn = self.conn()
        # tests = [['a','b','c'],['d','f','e']]
        cursor = conn.cursor()
        cursor.executemany(sql, sqlDataList)
        # lastrowid = cursor.lastrowid # 连接池下不支持
        conn.commit()
        cursor.close()
        # return lastrowid

    # def __del__(self):
    #     self.cursor.close()
    #     self.conn.close()


if __name__ == "__main__":
    WORD_DB = {
        "host": "10.10.11.244",
        "user": "biuser",
        "passwd": "@biuser123",
        "db": "userdata",
        "port": 3309,
    }
    mysql_client = MySqlClientPool(conn_dict=WORD_DB, cursorclass="dict")
    sql = "select * from userdata.dict_professionalterm limit 10"
    print(mysql_client.query(sql))
    # mysql_client = MySqlClient(conn_dict=WORD_DB, cursorclass="ss_dict")
    # sql = "select * from spider_data.question where source='太平洋'"
    # for x in mysql_client.query_cursor(sql):
    #     print(x)
