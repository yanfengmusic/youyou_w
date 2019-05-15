#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2019/5/5'

from selenium import webdriver
from time import sleep
import unittest

class Login(unittest.TestCase):
    '''
    禅道登录
    '''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
    def setUp(self):
        self.driver.get("http://127.0.0.1:82/zentao/user-login-L3plbnRhby8=.html")

    def is_login_success(self):
        try:
            text = self.driver.find_element_by_css_selector(".user-name").text
            return text
        except:
            return ""

    def is_alert_exist(self):
        try:
            sleep(3)
            alert = self.driver.switch_to_alert()
            text = alert.text
            sleep(2)
            alert.accept()
            return text
        except Exception as info:
            print(info)
            return ""


    def test_01_(self):
        '''
        用例1 登录成功
        :return:
        '''
        sleep(2)

        self.driver.find_element_by_css_selector("#account").send_keys("admin")
        self.driver.find_element_by_css_selector("[name='password']").send_keys("Yanfengmusic521")
        self.driver.find_element_by_css_selector("#submit").click()
        sleep(3)
        text = self.is_login_success()
        self.assertTrue(text=='admin')

    def test_02(self):
        '''
        用例2 登录失败
        '''
        sleep(2)
        self.driver.find_element_by_css_selector("#account").send_keys("admin")
        self.driver.find_element_by_css_selector("[name='password']").send_keys("Yanfengmusic52")
        self.driver.find_element_by_css_selector("#submit").click()
        sleep(3)
        text = self.is_login_success()
        print("登录失败，获取结果为%s" % text)
        # self.assertTrue(text=="")
        self.assertTrue(1 == 2)

    def tearDown(self):
        self.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# if __name__ == '__main__':
#     unittest.main()




