# -*- coding:utf-8 -*-
# @Time    :2019/10/31 0031 13:05
# @Author  :Antoy
# @Mail    :286075568@qq.com
# @FileName: testadd_sub.py
# @Software: PyCharm

# import unittest
# # 导入测试文件
# from UnittestOptimize import testadd,testsub
#
# # 构造测试集
# suite = unittest.TestSuite()
#
# suite.addTest(testadd.TestAdd("test_add"))
# suite.addTest(testadd.TestAdd("test_add2"))
#
# suite.addTest(testsub.TestSub("test_sub"))
# suite.addTest(testsub.TestSub("test_sub2"))
#
# if __name__ == '__main__':
#     # 执行测试
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
# # 上面这种组织用例的方法要比之前简洁一些，但是当用例更多的时候，我们还需要通过 addTest()方法将新增的用例添加到 test.py 文件中。我们讲解一个可以自动添加的方法。
# 这就是 TestLoader 类中提供的一个 discover()方法。
#
# TestLoader 负责根据各种标准加载测试用例，并将他们返回给测试套件。正常情况下，不需要创建这个类的实例。
# unittest 提供了可以共享的 defaultTestLoader 类，可以使用其子类和方法创建实例，discover()方法就是这个类中的一个方法之一。




import unittest

import HTMLTestRunner

from BeautifulReport import BeautifulReport
import sys,os
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(discover)

    # 写入txt文件
    # with open('UnittestTextReport.txt', 'a') as f:
    #     runner = unittest.TextTestRunner(stream=f, verbosity=2)
    #     runner.run(discover)

    # 运用HTMLTestRunner输出测试报告
    # with open('./Picture/HTMLReport.html', 'wb') as f:
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='Test Report',description='Report Details',verbosity=2)
    #     runner.run(discover)


    # 运用BeautifulReport输出测试报告，样式更好看    注：下载BeautifulReport的完整.ZIP文件，然后解压，把整个文件包放到本地python的/Lib/site-packages/目录下
    BeautifulReport(discover).report(filename='百度测试报告', description='调试unittest', log_path='.')




















        # # 定义测试报告的地址
        # path = 'D:\\AUTOTEST\\Python3\\BUGtest\\UnittestOptimize'
        # report_path = path + 'result.html'
        #
        # # 如果路径不存在，创建路径
        # if not os.path.exists(path):
        #     os.makedirs(path)
        # else:
        #     pass
        # fp = file(report_path, 'wb')
        # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'网管子系统Http接口测试报告', description='Report_description')
        #
        # # 执行测试
        # runner.run(discover)




# 这次的test.py可能就是 终极组织用例的方法了。现在我们介绍一下 discover()方法中参数的意思：
#
# test_dir:需要加载的单元测试文件的路径。因为我这里 test.py文件和和各个测试用例在同一路径下，所以test_dir = './'。如果不是在同一路径下，
# 就填写绝对路径，比如我的路径就应该是test_dir = /Users/guxuecheng/Desktop/unittest脚本
#
# patten 是一个正则表达式，pattern='test*.py'是指加载所有 test 开头的.py 文件，*表示任意多个字符。
#
# discover()方法会自动的根据测试目录（test_dir）匹配查找测试用例文件（test*.py)，并将查找到的测试用例组装到测试套件 suite 中，因此可以通过run()方法执行 discover。
#

