"""
@Time   : 2019/3/28
@author : lijc210@163.com
@Desc:  : 功能描述。
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://auth.p4p.sogou.com")
cookie_list = [
    {"name": "JSESSIONID", "value": "aaaJnVRvoz4w0-kVW2dNw"},
    {"name": "suf_p4p_user_id", "value": "20646737"},
    {"name": "uid", "value": "20646737"},
    {"name": "xuri_sid", "value": "d25c9eed-a91b-49f0-8e69-b3fc3238e37f"},
]

for cookie in cookie_list:
    print(cookie)
    driver.add_cookie(cookie)

print(driver.current_url)
driver.get("http://xuri.p4p.sogou.com/cpcadindex/init2.action#/index")
print(driver.current_url)
