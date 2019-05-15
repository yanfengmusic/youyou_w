#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2019/5/9'

url = "http://127.0.0.1:82/zentao/user-login-L3plbnRhby8=.html"

import unittest
from selenium import  webdriver
from page.add_bug_page import AddBugPage
from page.login_page import Base
from page.login_page import LoginPge
import time

class Test_ADD_Bug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        # cls.bug = Base(cls.driver)
        cls.add = AddBugPage(cls.driver)
        cls.denglu = LoginPge(cls.driver)
        cls.denglu.login()

    # 保证每一条用例操作完后，都回到指定的起点
    def setUp(self):
        self.driver.get(url)

    def test_add_bug(self):
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = "测试提交的bug" + timestr
        self.add.add_bug(title)
        result = self.add.is_add_bug_success(title)
        print(result)
        self.assertTrue(result)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()





