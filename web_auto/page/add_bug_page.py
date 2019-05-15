#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2019/5/9'

from selenium import webdriver
from common.base import Base
import time

class AddBugPage(Base):
    loc_test=("link text","测试")
    loc_bug =("xpath",".//*[@id='subNavbar']/ul/li[1]/a")
    # loc_add =("xpath",".//*[@id='mainContent']/div[2]/div[2]/p/a")
    loc_add = ("xpath", ".//*[@id='mainMenu']/div[3]/a[3]/i")
    loc_mokuai=("xpath",".//*[@id='module_chosen']/a/span")
    loc_mokuai2=("xpath",".//*[@id='module_chosen']/div/ul/li[2]")
    loc_project = ("xpath",".//*[@id='project_chosen']/a/span")
    loc_project2=("xpath",".//*[@id='project_chosen']/div/ul/li")
    loc_truck = ("xpath",".//*[@id='openedBuild_chosen']/ul")
    loc_truck2=("xpath",".//*[@id='openedBuild_chosen']/div/ul/li")
    loc_leixing1=("xpath",".//*[@id='type_chosen']/a/div[1]")
    loc_leixing2=("xpath",".//*[@id='type_chosen']/div/ul/li[2]")
    loc_biaoti=("id","title")
    loc_content=("xpath","html/body")
    loc_save=("id","submit")
    loc_yzTitle=("xpath",".//*[@id='bugList']/tbody/tr[1]/td[4]/a")

    # def __init__(self,driver:webdriver.Firefox):
    #     self.driver=driver
    #     self.zentao = Base(self.driver)

    def add_bug(self,title):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_add)
        self.click(self.loc_mokuai)
        self.click(self.loc_mokuai2)
        self.click(self.loc_truck)
        self.click(self.loc_truck2)
        self.click(self.loc_project)
        self.click(self.loc_project2)
        self.click(self.loc_leixing1)
        self.click(self.loc_leixing2)

        self.sendKeys(self.loc_biaoti,title)
        frame = self.findElement(("class name","ke-edit-iframe"))
        # 富文本不能clear()
        self.driver.switch_to_frame(frame)
        self.sendKeys(self.loc_content,"测试测试测试测试测试")
        self.driver.switch_to_default_content()
        self.click(self.loc_save)

    def is_add_bug_success(self,_text):
        return self.is_text_in_element(self.loc_yzTitle,_text)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    bug = AddBugPage(driver)

    from page.login_page import LoginPge
    login = LoginPge(driver)
    login.login()

    timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
    title = "测试提交的bug"+timestr
    bug.add_bug(title)
    result = bug.is_add_bug_success(title)
    print(result)


















