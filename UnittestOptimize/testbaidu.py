# -*- coding:utf-8 -*-
# @Time    :2019/10/31 0031 14:49
# @Author  :Antoy
# @Mail    :286075568@qq.com
# @FileName: testbaidu.py
# @Software: PyCharm
import time,unittest
from selenium import webdriver


class TestAdd(unittest.TestCase):

   def setUp(self):
       print()

   def tearDown(self):
       print()
   def test_Ui(self):
            u'''UI的测试，同时生成报告和图片'''
            # executable_path = r'C:\Users\fmj\AppData\Local\Google\Chrome\Application\chromedriver.exe'
            # driver = webdriver.Chrome(executable_path)
            driver = webdriver.Chrome()
            driver.get("http://www.baidu.com")
            driver.get_screenshot_as_file("./Picture/login_success.jpg")

            print(driver.title)
            self.assertEqual(driver.title, u'百度一下，你就知道')
            time.sleep(3)
            driver.close()


if __name__ == '_main__':
    unittest.main()