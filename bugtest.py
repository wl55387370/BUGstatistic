# -*- coding:utf-8 -*-
# @Time    :2019/10/18 0018 13:13
# @Author  :Antoy
# @Mail    :286075568@qq.com
# @FileName: bugtest.py
# @Software: PyCharm

# 导入selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 导入csv包
import csv, time
import os
# 发送邮件
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import pandas as pd





# 判断c盘是否有该文件

ft=os.path.exists("C:\\Users\\Administrator\\Downloads\\新零售-未解决Bug.csv")
if (ft) :
    os.remove("C:\\Users\\Administrator\\Downloads\\新零售-未解决Bug.csv")
    print("删除文件成功！")
else:
    print("无指定文件！获取指定文件")

# 获开始时间
starttime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

print("开始时间："+str(starttime))
#打开浏览器

driver=webdriver.Chrome()

#访问禅道
driver.get("http://zentao.iwubida.com/user-login.html")

#登录
driver.find_element_by_id("account").send_keys("wulin")
driver.find_element_by_name("password").send_keys("kt7c9lO%RGrN")
#通过不同的定位方式点击登录按钮
driver.find_elements_by_class_name("btn-primary")[0].click()
#driver.find_elements_by_class_name("btn")[1].click()
#driver.find_element_by_class_name("btn btn-primary").click()
# driver.find_element_by_id("submit").click()

#点击测试
driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[4]/a').click()
#点击bug
driver.find_element_by_xpath('//*[@id="subNavbar"]/ul/li[1]/a').click()
#点击类型
driver.find_element_by_xpath('//*[@id="currentItem"]').click()
driver.find_element_by_xpath('//*[@id="dropMenu"]/div[1]/input').send_keys("新零售")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="dropMenu"]/div[2]/div/div[1]/div[1]/a[5]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="mainMenu"]/div[2]/a[7]/span').click()

#点击导出csv文件
driver.find_element_by_xpath('//*[@id="mainMenu"]/div[3]/div/button/span[1]').click()
driver.find_element_by_xpath('//*[@id="exportActionMenu"]/li/a').click()
#切入iframe
driver.switch_to.frame(driver.find_element_by_id('iframe-triggerModal'))
time.sleep(3)
driver.find_element_by_id('encode').send_keys("GBK")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="submit"]').click()
time.sleep(10)
# 切出
# driver.switch_to_default_content()
driver.close()
print("浏览器关闭")


# 读取下载的文件


out = open("C:\\Users\\Administrator\\Downloads\\新零售-未解决Bug.csv", 'r')

read_csv = csv.reader(out, dialect='excel')
# 统计未解决的总数
totalcount1 = 0
# 统计严重条数
totalserious = 0

for line in read_csv:  # 循环输出csv中的所有数据
    totalcount1 = totalcount1 + 1

    if line[9] == "2":
        totalserious = totalserious + 1

# print(line)
totalcount = totalcount1 - 1
print("未解决BUG总数：" + str(totalcount))
print("严重BUG数量：" + str(totalserious))

# 获取结束时间
endtime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print("结束时间："+str(endtime))
out.close()

# 等待发送邮件
# 发件人和收件人
sender = 'm18570394312_1@163.com'
receiver = '286075568@qq.com'

# 所使用的用来发送邮件的SMTP服务器
smtpserver = 'smtp.163.com'

# 发送邮箱的用户名和授权码（不是登录邮箱的密码）
username = 'm18570394312_1@163.com'
password = 'dongnao001'

# 邮件主题
mail_title = '未解决BUG统计'

# 读取html文件内容

f = open('BUGmail.html', 'rb+')
# HTML文件默认和当前文件在同一路径下，若不在同一路径下，需要指定要发送的HTML文件的路径
rd=f.read()
rd = rd.decode('utf-8')
rd = rd.replace('title', str(mail_title))
rd = rd.replace('totalserious', str(totalserious))
rd = rd.replace('totalcount', str(totalcount))
rd = rd.replace('starttime', str(starttime))
rd = rd.replace('endtime', str(endtime))
mail_body =rd
f.close()


# 邮件内容, 格式, 编码
message = MIMEText(mail_body, 'html', 'utf-8')
message['From'] = sender
message['To'] = receiver
message['Subject'] = Header(mail_title, 'utf-8')

try:
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, message.as_string())
    print("发送邮件成功！！！")
    smtp.quit()
except smtplib.SMTPException:
    print("发送邮件失败！！！")
