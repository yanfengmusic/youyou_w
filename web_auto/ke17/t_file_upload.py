#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pykeyboard import PyKeyboard
from pymouse import PyMouse
import time
from page.login_page import LoginPge


from page.login_page import LoginPge
from selenium import webdriver

driver = webdriver.Firefox()
a = LoginPge(driver)
a.login()

# 直接打开编辑页面
driver.get("http://127.0.0.1:82/zentao/bug-create-1-0-moduleID=0.html")
# 如果加载慢的时候会出错，所以在这里需要加入sleep方法等待一会
time.sleep(3)
driver.find_element_by_css_selector(".ke-toolbar-icon.ke-toolbar-icon-url.ke-icon-image").click()
time.sleep(3)
driver.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/div/div[1]/ul/li[2]").click()
# driver.find_element_by_css_selector(".ke-tabs-li.ke-tabs-li-on").click()
time.sleep(2)

# 点击浏览
driver.find_element_by_css_selector(".ke-inline-block.ke-upload-button").click()
time.sleep(2)

# 默认在取消按钮上，先切换到保存文件上
k = PyKeyboard()
path="e:\hello.xlsx"
for i in path:
    k.tap_key(i)
time.sleep(2)
k.tap_key(k.enter_key)
time.sleep(2)
k.tap_key(k.enter_key)
time.sleep(2)
k.tap_key(k.enter_key)
time.sleep(1)
driver.find_element_by_xpath("html/body/div[3]/div[1]/div[3]/span[1]/input").click()

# 轻轻按下然后放开,回车
# k.tap_key(k.enter_key)
# 发送tab
# k.press_key(k.tap_key)
# k.release_key(k.tap_key)
# 发送回车
