# -*- coding:utf-8 -*-
# @Time    :2019/10/30 0030 15:37
# @Author  :Antoy
# @Mail    :286075568@qq.com
# @FileName: testcount.py
# @Software: PyCharm

from Unittest.count import is_prime
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print("测试开始")

    def tearDown(self):
        print("测试结束")

    def test_case(self):
        self.assertTrue(is_prime(9), msg="is Not Prime")


if __name__ == "__main__":
    unittest.main()