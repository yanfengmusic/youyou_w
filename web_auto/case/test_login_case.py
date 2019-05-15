#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from page.login_page import LoginPge,login_url
from selenium import webdriver

__mtime__ = '2019/5/9'
"""
1.输入admin，输入密码，点击登录  期望结果：
2.输入admin,不输入密码，点击登录
3.输入admin，输入密码，点击记住登录，点击登录
4.点击忘记密码

"""
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginP = LoginPge(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.driver.maximize_window()
        self.loginP.is_alert()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    # 输入admin，输入密码，点击登录  期望结果：
    def test_01(self):
        self.loginP.input_user("admin")
        self.loginP.input_psw("Yanfengmusic521")
        self.loginP.click_login_button()
        result = self.loginP.get_user_name()
        self.assertTrue(result=="admin")


    # 输入admin,不输入密码，点击登录
    def test_02(self):
        self.loginP.input_user("admin")
        self.loginP.click_login_button()
        result = self.loginP.get_user_name()
        self.assertTrue(result == "")


    # 输入admin，输入密码，点击记住登录，点击登录
    def test_03(self):
        self.loginP.input_user("admin")
        self.loginP.input_psw("Yanfengmusic521")
        self.loginP.click_keep_login()
        self.loginP.click_login_button()
        result = self.loginP.get_user_name()
        self.assertTrue(result == "admin")

    # 忘记密码
    def test_04(self):
        self.loginP.forget_psw()
        result = self.loginP.is_refresh_exist()
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()








