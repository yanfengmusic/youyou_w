#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2019/5/9'
from selenium import webdriver
from common.base import Base
import time

login_url="http://127.0.0.1:82/zentao/user-login.html"

class LoginPge(Base):
    # 定位登录
    loc_username = ("id","account")
    loc_passwd=("name","password")
    loc_submit=("css selector","#submit")
    loc_keep_login=("xpath",".//*[@id='keepLoginon']")
    loc_forget_psw=("link text","忘记密码")
    loc_login_text = ("css selector",".user-name")
    loc_forget_psw_page = ("css selector", ".btn.btn-primary.btn-wide")

    def input_user(self,text):
        self.sendKeys(self.loc_username,text)
    def input_psw(self,text):
        self.sendKeys(self.loc_passwd,text)
    def click_login_button(self):
        self.click(self.loc_submit)
    def click_keep_login(self):
        self.click(self.loc_keep_login)
    def forget_psw(self):
        self.click(self.loc_forget_psw)


    def get_user_name(self):
        """
        获取登录的名称
        :return:
        """
        user = self.get_text(self.loc_login_text)
        return user

    def is_alert_exist(self):
        a = self.is_alert()
        if  a:
            print(a.text)
            a.accept()

    #     判断忘记密码页，刷新按钮是否存在
    def is_refresh_exist(self):
        r = self.isElementExist(self.loc_forget_psw_page)
        print(r)
        return r

    # 专门封装一个登陆方法
    # 加一个开关的小技巧
    def login(self, user="admin", psw="Yanfengmusic521",keep_login=False):
        self.driver.get(login_url)
        self.driver.maximize_window()
        self.sendKeys(self.loc_username, "admin")
        self.sendKeys(self.loc_passwd, psw)
        if keep_login:
            self.click_keep_login()
        self.click(self.loc_submit)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    login_page = LoginPge(driver)
    # driver.get(login_url)
    # login_page.input_user("admin")
    # login_page.input_psw("Yanfengmusic521")
    # login_page.click_keep_login()
    # login_page.click_login_button()
    # login_page.forget_psw()
    # login_page.is_refresh_exist()

    # 加一个开关的小技巧
    login_page.login(keep_login=True)
    login_page.login()

