import psycopg2
import pymysql
import requests
from dbutils.pooled_db import PooledDB


#  快排
def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


# 冒泡排序
def bubbleSort(arr):
    """
    冒泡排序
    param arr: 待排序数组
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# 测试 bubbleSort
def test_bubbleSort():
    arr = [1, 3, 2, 5, 4]
    print(bubbleSort(arr))


# 从1到100的数组
alist = list(range(1, 101))

# 解释bubbleSort原理
# bubbleSort: 1. 从第一个元素开始，依次比较相邻的两个元素，如果前一个元素比后一个元素大，则交换两个元素的位置。

# 英语Found inline suggestions locally
# 翻译中文: 在本地找到内联建议
# 翻译韩文: 로컬에서 인라인 제안을 찾았습니다.


# 使用requests库请求www.baidu.com
def get_baidu():
    r = requests.get("http://www.baidu.com")
    print(r.text)
    print(r.status_code)
    print(r.encoding)
    print(r.headers)
    print(r.cookies)
    print(r.url)
    print(r.history)
    print(r.links)
    print(r.raw)
    print(r.raw.read(10))
    print(r.raw.read(10))


# 查询mysql的工具类


class MysqlUtil:
    def __init__(self, host, port, user, password, db, charset="utf8"):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset=self.charset,
        )
        self.cursor = self.conn.cursor()
        self.conn.autocommit(True)

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def insert(self, sql):
        self.cursor.execute(sql)

    def update(self, sql):
        self.cursor.execute(sql)

    def delete(self, sql):
        self.cursor.execute(sql)

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()


# mysql连接池工具类


class MysqlPoolUtil:
    def __init__(
        self, host, port, user, password, db, charset="utf8", maxconnections=10
    ):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.maxconnections = maxconnections
        self.pool = PooledDB(
            pymysql,
            maxconnections,
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset=self.charset,
        )

    def query(self, sql):
        conn = self.pool.connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def insert(self, sql):
        conn = self.pool.connection()
        cursor = conn.cursor()
        cursor.execute(sql)

    def update(self, sql):
        conn = self.pool.connection()
        cursor = conn.cursor()
        cursor.execute(sql)

    def delete(self, sql):
        conn = self.pool.connection()
        cursor = conn.cursor()
        cursor.execute(sql)

    def commit(self):
        conn = self.pool.connection()
        conn.commit()

    def rollback(self):
        conn = self.pool.connection()
        conn.rollback()


# 查询postgresql的工具类
class PostgresqlUtil:
    def __init__(self, host, port, user, password, db, charset="utf8"):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset=self.charset,
        )
        self.cursor = self.conn.cursor()
        self.conn.autocommit = True

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def insert(self, sql):
        self.cursor.execute(sql)

    def update(self, sql):
        self.cursor.execute(sql)

    def delete(self, sql):
        self.cursor.execute(sql)

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()


# 表名 shop_sales,字段有amount销售金额，shop_code销售门店编码，city城市,查询每个城市平均销售额
# select city, avg(amount) from shop_sales group by city

# 查询每个城市的销售额最大的门店
# select city, shop_code, max(amount) from shop_sales group by city

#  查询每个城市销售额排名前五的门店,数据库为clickhouse，使用窗口函数
# select city, shop_code, amount from (select city, shop_code, amount, row_number() over(partition by city order by amount desc) as rank from shop_sales) where rank <= 5
