# -*- coding: utf-8 -*-
# @Time     : 2020/9/13
# @Author   : Bruce lee
# @function : 16进制转换为10进制输出


# 方法一
while True:
    try:
        print(eval(input()))
    except:
        break


# 方法二
while True:
    try:
        print(int(input(), 16))
    except:
        break
