# -*- coding:utf-8 -*-
# @Time    :2019/10/31 0031 11:18
# @Author  :Antoy
# @Mail    :286075568@qq.com
# @FileName: testsub.py
# @Software: PyCharm

from UnittestOptimize.calculator import Count
import unittest


class TestSub(unittest.TestCase):

    def setUp(self):
        print()

    def tearDown(self):
        print()

    def test_sub(self):
        # Count类有两个参数，创建对象的时候要有两个参数。
        s = Count(10,4)
        self.assertEqual(s.sub(), 5, msg="实际结果和预期不符")

    def test_sub2(self):
        s = Count(19, 14)
        self.assertEqual(s.sub(), 5)

    if __name__ == '_main__':
        unittest.main()