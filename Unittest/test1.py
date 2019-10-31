# -*- coding:utf-8 -*-
# @Time    :2019/10/30 0030 15:24
# @Author  :Antoy
# @Mail    :286075568@qq.com
# @FileName: test1.py
# @Software: PyCharm


import unittest


class Count(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b


# 计算加法
    def add(self):
        return self.a + self.b


# 单元测试，测试 add()方法
class TestCount(unittest.TestCase):

    def setUp(self):
        print("Test Start")

    def test_add(self):
        # 这里参数3，4是我们写死的，实际是可能变化不固定的。比如将读取到的表格内的数据当做这两个参数。
        s = Count(3,4)
        # 这里的比较对象5就是我们的预期结果，与之不同即为 Fail。
        self.assertEqual(s.add(),5)

    def tearDown(self):
        print("Test end")

    if __name__ == '__main__':
        unittest.main()