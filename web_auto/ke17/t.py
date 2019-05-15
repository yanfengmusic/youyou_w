#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from pykeyboard import PyKeyboard

__mtime__ = '2019/5/15'

time.sleep(2)
k = PyKeyboard()
path="e:\hello.xlsx"
for x in path:
   k.tap_key(x)



