# -*- coding:utf-8 -*-
# @Time    :2019/10/30 0030 15:26
# @Author  :Antoy
# @Mail    :286075568@qq.com
# @FileName: testcalculator.py
# @Software: PyCharm

from Unittest.calculator import Count
# 单元测试必须要引入unittest模块
import unittest


#单元测试的重要概念
#1. TestCase
#一个TestCase的实例就是一个测试用例。一个测试用例要包括测试前准备环境的搭建(setUp)，执行测试代码(run)，以及测试后环境的还原(tearDown)。一个测试用例是一个完整的测试单元，通过运行这个测试单元，可以对某一个功能进行验证。

#2. TestSuite

#对于某一个功能模块的验证可能需要多个测试用例，多个测试用例集合在一起执行验证某一个功能，这样就是一个TestSuite。通过addTest()方法将 TestCase 加载到 TestSuite()中。

#3. TestRunner
#TestRunner可以使用图形界面、文本界面，或返回一个特殊的值等方式来表示测试执行的结果。TextTestRunner提供的 run()方法来执行 test suite/test case。

#4.TestFixture
#一个测试用例环境的搭建和销毁就是一个 fixture。




# 测试方法必须要继承自unittest.TestCase
# class TestCount(unittest.TestCase):
#
#     def setUp(self):
#         print("Test Start测试开始")
#
#     def test_add(self):
#         s = Count(3, 4)
#         self.assertEqual(s.add(), 5)
#
#     def tearDown(self):
#         print("Test end测试结束")
#
#
# if __name__ == '__main__':
#     unittest.main()
# class TestCount(unittest.TestCase):
#
#
#     def setUp(self):
#         print("测试开始")
#
#     def tearDown(self):
#         print("测试结束")
#
#     def test_add(self):
#         s = Count(2, 1)
#         self.assertEqual(s.add(), 3)
#
#         # print("用例1")
#
#     def test_add2(self):
#         s = Count(2, 3)
#         self.assertEqual(s.add(), 5)
#
#         # print("用例2")
#
#
# class TestSub(unittest.TestCase):
#     def setUp(self):
#         print("测试减法开始")
#
#     def tearDown(self):
#         print("测试减法结束")
#
#     def test_sub(self):
#         s = Count(4, 1)
#         self.assertEqual(s.sub(), 2, msg="4 - 1 != 2")
#
#     def test_sub2(self):
#         s = Count(3, 1)
#         self.assertEqual(s.sub(), 2)
#
#
# if __name__ == '__main__':
#     print("到这了")
#     #  构造测试集
#     suite = unittest.TestSuite()
#     suite.addTest(TestCount.test_add())
#     suite.addTest(TestCount.test_add2())
#     suite.addTest(TestSub.test_sub())
#     suite.addTest(TestSub.test_sub2())
#     # 执行测试
#     runner = unittest.TextTestRunner()
#     runner.run(suite)



#优化代码
#通过观察上面的脚本还是有重复代码，我们可以继续修改
class MyTest(unittest.TestCase):

    def setUp(self):
        print("测试开始")

    def tearDown(self):
        print("测试结束")


class TestCount(MyTest):

    def test_add(self):
        s = Count(2,1)
        self.assertEqual(s.add(), 3)
    print("用例1")

    def test_add2(self):
        s = Count(2,3)
        self.assertEqual(s.add(), 5)
    print("用例2")


class TestSub(MyTest):

    def test_sub(self):
        s = Count(4, 1)
        self.assertEqual(s.sub(), 3, msg="错误原因：4 - 1 != 2")

    print("用例3")

    def test_sub2(self):
        s = Count(3, 1)
        self.assertEqual(s.sub(), 2)

    print("用例4")


if __name__ == '__main__':
        print("到这了")
        #  构造测试集
        suite = unittest.TestSuite()
        suite.addTest(TestCount.test_add())
        suite.addTest(TestCount.test_add2())
        suite.addTest(TestSub.test_sub())
        suite.addTest(TestSub.test_sub2())
        # 执行测试
        runner = unittest.TextTestRunner()
        runner.run(suite)
