#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

__mtime__ = '2019/5/9'

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("file:///E:/ChargeTime/HTML/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")
driver.maximize_window()
sleep(3)
#自动判断高度滚动到底部
# js = "window.scrollTo(0,document.body.scrollHeight)"
# driver.execute_script(js)
# sleep(3)
# #自动判断高度滚动到顶部
# js = "window.scrollTo(0,0)"
# driver.execute_script(js)
# 滚动到元素出现的位置
ele=driver.find_element_by_css_selector("#gw")
driver.execute_script("arguments[0].scrollIntoView();",ele)

