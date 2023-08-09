"""
@Time   : 2019/3/28
@author : lijc210@163.com
@Desc:  : 功能描述。
"""
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("lang=zh_CN.UTF-8")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("enable-web-security")

driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('https://auth.p4p.sogou.com/login?service=http://xuri.p4p.sogou.com')
driver.get("http://xuri.p4p.sogou.com/cpcadindex/init2.action#/index")

print(driver.get_cookies())
login_cookie_list = driver.get_cookies()
print("aaaaaa", json.dumps(login_cookie_list))

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

cookie_list.extend(login_cookie_list)
print("bbbbb", json.dumps(cookie_list))

for cookie in cookie_list:
    print(cookie)
    cookie.pop("domain")
    driver.add_cookie(cookie)

print(driver.get_cookies())

driver.get("http://xuri.p4p.sogou.com/cpcadindex/init2.action#/index")
print(driver.title)
