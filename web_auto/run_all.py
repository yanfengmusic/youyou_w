#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2019/5/5'

import unittest
from common import HTMLTestRunner_cn

casePath = "D:\\Tools\\Python\\PycharmProjects\\web_auto\\case"
rule="test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)
reportPath = "D:\Tools\\Python\\PycharmProjects\\web_auto\\report"+"report.html"
fp = open(reportPath,'wb')
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="报告的title",description="描述你报告时干什么用啊",retry=1)
runner.run(discover)
fp.close()

