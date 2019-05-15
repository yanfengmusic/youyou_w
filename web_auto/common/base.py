from selenium import webdriver
from time import sleep

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Base():
    def __init__(self,driver:webdriver.Firefox):
        self.driver = driver
        self.timeout=10
        self.t = 0.5

    # 使用EC的方式进行查找元素，找到了返回这个元素，找不到提示超时异常
    def findEleByEC(self,locator):
        ele = WebDriverWait(self.driver, self.timeout,self.t).until(EC.presence_of_element_located(locator))
        return ele


    def findElement(self,locator):
        ele = WebDriverWait(self.driver, self.timeout,self.t).until(lambda x: x.find_element(*locator))
        # element = WebDriverWait(driver, 10,1).until(lambda x: x.find_element_by_id("someId"))
        return ele

    def findElements(self,locator):
        # element = WebDriverWait(driver, 10,1).until(lambda x: x.find_element_by_id("someId"))
        eles = WebDriverWait(self.driver, self.timeout,self.t).until(lambda x: x.find_elements(*locator))
        return eles

    def sendKeys(self,locator,text):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self,locator):
        ele = self.findElement(locator)
        ele.clear()

    def isSelected(self,locator):
        '''
       判断元素是否被选中
        '''''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return

    # 判断元素是否存在第一种方法
    def isElementExist(self,locator):
        try:
            ele=self.findElement(locator)
            return True
        except Exception as info:
            print(info)
            return False

    # 判断元素是否存在第二种方法
    def isElementExist2(self,locator):
        eles=self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n ==1:
            return True
        else:
            print("定位到元素的个数：%d" % n)
            return True

# 使用EC的方法判断title的方法1：EC.title_is(_title)
    def is_title(self,_title):
        """
        :param _title: 为期望结果
        :return: 返回的结果为True和False
        """
        try:
            result= WebDriverWait(self.driver, self.timeout,self.t).until(EC.title_is(_title))
            return result
        except:
            return False

# 使用EC的方法判断title的方法2：EC.title_contains(_title)
    def is_title_contains(self,_title):
        """
        :param _title: 为期望结果
        :return: 返回的结果为True和False
        """
        try:
            result= WebDriverWait(self.driver, self.timeout,self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

# 判断文本是不是在这个元素里面
    def is_text_in_element(self,locator,_text):
        """
        判断文本是不是在这个元素里面
        :param _text: 希望结果
        :return: True和False
        """
        try:
            result= WebDriverWait(self.driver, self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    # 判断一个元素的value属性值
    def is_value_in_element(self,locator,_value):
        """
        :param locator:
        :param value:
        :return: 空和错误都是返回False,正确则返回True
        """
        try:
            result = WebDriverWait(self.driver, self.timeout,self.t).until(EC.text_to_be_present_in_element_value(locator,_value))
            return result
        except:
            return False

    def is_alert(self):
        """
        :return: 如果有则返回alert对象，调用该方法后，可以根据alert对象获取到该对象属性值
        """
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_text(self,locator):
        """
        获取元素的文本信息
        :param locator: 定位
        :return: 成功返回元素的文本信息，失败返回空
        """
        try:
            t = self.findElement(locator).text
            return t
        except:
            print("获取文本失败，返回'' ")
            return ""

#     封装鼠标悬停事件
    def move_to_element(self,locator):
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element()

#      封装select方法 index value和文本
#     需要先定位到select标签
    def select_by_index(self,locator,index=0):
        ele = self.findElement(locator)
        Select(ele).select_by_index(index)
    def select_by_valuex(self,locator,value):
        ele = self.findElement(locator)
        Select(ele).select_by_value(value)
    def select_by_text(self,locator,text):
        ele = self.findElement(locator)
        Select(ele).select_by_visible_text(text)

    # 浏览器js操作滚动条
    # 聚焦到指定的元素位置
    def js_focus_element(self,locator):
        target = self.findElement(locator)
        driver.execute_script("arguments[0].scrollIntoView();",target)
    # 滚动到顶部
    def js_scroll_top(self):
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)
    # 滚动到底部
    def js_scroll_top(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        driver.execute_script(js)
    # 横向滚动
    def js_scroll_Hengxiang(self,x=0):
        js = "window.scrollTo(%s,document.body.scrollHeight)" %x
        driver.execute_script(js)











if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:82/zentao/user-login-L3plbnRhby8=.html")
    zentao = Base(driver)
    # loc1 = (By.ID, "account")
    # loc2 = (By.NAME, "password")
    # loc3 = (By.CSS_SELECTOR, "#submit")

    loc1 = ("id","account");
    loc2 = ("name","password")
    loc3 = ("css selector","#submit")
    zentao.sendKeys(loc1,"admin")
    zentao.sendKeys(loc2,"Yanfengmusic521")
    zentao.click(loc3)

