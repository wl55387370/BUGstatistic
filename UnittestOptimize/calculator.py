# -*- coding:utf-8 -*-
# @Time    :2019/10/30 0030 15:26
# @Author  :Antoy
# @Mail    :286075568@qq.com
# @FileName: calculator.py
# @Software: PyCharm

import unittest

class Count(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b


# 计算加法
    def add(self):
        return self.a + self.b


# 计算减法
    def sub(self):
        return self.a - self.b