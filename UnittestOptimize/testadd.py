# -*- coding:utf-8 -*-
# @Time    :2019/10/31 0031 11:17
# @Author  :Antoy
# @Mail    :286075568@qq.com
# @FileName: testadd.py
# @Software: PyCharm

from UnittestOptimize.calculator import Count
import unittest


class TestAdd(unittest.TestCase):

   def setUp(self):
       print()

   def tearDown(self):
       print()

   def test_add(self):
       # Count类有两个参数，创建对象的时候要有两个参数。
       s = Count(2,4)
       self.assertEqual(s.add(), 6, msg="实际结果和预期不符")

   def test_add2(self):
       s = Count(1, 4)
       self.assertEqual(s.add(), 5)

   if __name__ == '_main__':
       unittest.main()