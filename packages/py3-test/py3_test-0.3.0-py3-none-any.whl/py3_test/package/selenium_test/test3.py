"""
@Time   : 2019/3/28
@author : lijc210@163.com
@Desc:  : 功能描述。
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

COOKIE = """suf_p4p_user_id=20646737; xuri_sid=d25c9eed-a91b-49f0-8e69-b3fc3238e37f; JSESSIONID=aaaJnVRvoz4w0-kVW2dNw; uid=20646737"""

chrome_options = Options()
chrome_options.add_argument("lang=zh_CN.UTF-8")
chrome_options.add_argument(
    "User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
)
chrome_options.add_argument("Referer=http://xuri.p4p.sogou.com/cpcadindex/init2.action")
chrome_options.add_argument("Host=xuri.p4p.sogou.com")
chrome_options.add_argument("Accept-Encoding=gzip, deflate, br")
chrome_options.add_argument("Accept-Language=zh-CN,zh;q=0.9")
chrome_options.add_argument(
    "Content-Type=application/x-www-form-urlencoded; charset=UTF-8"
)
chrome_options.add_argument("Cookie={}".format(COOKIE))

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://xuri.p4p.sogou.com/cpcadindex/init2.action#/index")
print(driver.get_cookies())
print(driver.title)

cookie_list = [
    {
        "domain": "xuri.p4p.sogou.com",
        "expiry": 1553910460,
        "httpOnly": False,
        "name": "suf_p4p_user_id",
        "path": "/",
        "secure": False,
        "value": "20646737",
    },
    {
        "domain": "xuri.p4p.sogou.com",
        "httpOnly": False,
        "name": "uid",
        "path": "/cpcadindex",
        "secure": False,
        "value": "20646737",
    },
    {
        "domain": ".xuri.p4p.sogou.com",
        "httpOnly": False,
        "name": "xuri_sid",
        "path": "/",
        "secure": False,
        "value": "9a9cf6ed-e4a7-4830-8311-51cc7f0dbae9",
    },
    {
        "domain": "xuri.p4p.sogou.com",
        "httpOnly": False,
        "name": "JSESSIONID",
        "path": "/",
        "secure": False,
        "value": "aaa5ln2gC1RGD--xb2dNw",
    },
]

# for cookie in cookie_list:
#     print(cookie)
#     driver.add_cookie(cookie)

time.sleep(2)
driver.refresh()
print(driver.title)
print(driver.get_cookies())
