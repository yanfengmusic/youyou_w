
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

__mtime__ = '2019/5/11'

from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.12306.cn/index/")
driver.maximize_window()
driver.implicitly_wait(5)
js_remove = """
            document.getElementById("train_date").removeAttribute("readonly");
            document.getElementById("train_date").value="2019-09-29"
            """
driver.execute_script(js_remove)
sleep(3)

# 或者两者相结合使用
driver.find_element_by_id("train_date").clear()
driver.find_element_by_id("train_date").send_keys("2019-10-10")


