"""
Created on 2017/8/15 0015
@author: lijc210@163.com
Desc: 功能描述。
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")

# action = ActionChains(driver).move_to_element('//*[@id="lg"]/map/area')#移动到该元素
# action.context_click('//*[@id="lg"]/map/area')#右键点击该元素
# action.send_keys(Keys.ARROW_DOWN)#点击键盘向下箭头
# action.send_keys('v')#键盘输入V保存图
# action.perform()#执行保存

browser = webdriver.PhantomJS()
# browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
btn = browser.find_element_by_id("lg").find_element_by_tag_name("img")
ActionChains(browser).context_click(btn).send_keys("V").perform()
