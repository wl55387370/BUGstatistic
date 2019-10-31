# -*- coding:utf-8 -*-
# @Time    :2019/10/30 0030 15:37
# @Author  :Antoy
# @Mail    :286075568@qq.com
# @FileName: count.py
# @Software: PyCharm

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:

            print("i ====哈啊哈哈哈=== %s,%s" % (i, n))
            print(len(range(2, n)))

            return False
        print("i ====哈啊哈哈wo哈=== %s,%s" % (i, n))
        print(len(range(2, n)))
        return True