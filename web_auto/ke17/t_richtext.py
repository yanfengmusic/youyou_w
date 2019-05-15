#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

__mtime__ = '2019/5/11'

from page.login_page import LoginPge
from selenium import webdriver

driver = webdriver.Firefox()
a = LoginPge(driver)
a.login()

# 直接打开编辑页面
driver.get("http://127.0.0.1:82/zentao/bug-create-1-0-moduleID=0.html")
# 如果加载慢的时候会出错，所以在这里需要加入sleep方法等待一会
sleep(3)

body = "步骤：" \
       "结果" \
       "期望结果"
js='document.getElementsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML=("%s")'% body
driver.execute_script(js)


