#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from page.login_page import LoginPge,login_url
from selenium import webdriver
import ddt

__mtime__ = '2019/5/9'
"""
1.输入admin，输入密码，点击登录  期望结果：
2.输入admin,不输入密码，点击登录
3.不输入admin，输入密码，点击登录
"""
testdata = [
    {"user":"admin","psd":"Yanfengmusic521","expect":"admin"},
    {"user":"admin","psd":"","expect":""},
    {"user":"","psd":"Yanfengmusic","expect":""}
            ]

@ddt.ddt
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

    def login(self,user,psw,expect):
        self.loginP.input_user(user)
        self.loginP.input_psw(psw)
        self.loginP.click_login_button()
        result = self.loginP.get_user_name()
        print("测试结果为：%s" % result)
        self.assertTrue(result == expect)


    # 输入admin，输入密码，点击登录  期望结果：
    @ddt.data(*testdata)
    def test_01(self,data):
        print("-------------开始测试1-----------------")
        print("测试数据为：%s" %data)
        self.login(data["user"],data["psd"],data["expect"])
        print("-------------结束测试1-----------------")

    # # 输入admin,不输入密码，点击登录
    # def test_02(self):
    #     print("-------------开始测试2-----------------")
    #     data2 = testdata[1]
    #     print("测试数据为：%s" % data2)
    #     self.login(data2["user"], data2["psd"], data2["expect"])
    #     print("-------------结束测试2-----------------")
    #
    # # 输入admin，输入密码，点击记住登录，点击登录
    # def test_03(self):
    #     print("-------------开始测试3-----------------")
    #     data3 = testdata[2]
    #     print("测试数据为：%s" % data3)
    #     self.login(data3["user"], data3["psd"], data3["expect"])
    #     print("-------------结束测试3-----------------")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

