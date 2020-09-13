# -*- coding: utf-8 -*-
# @Time    : 2020/9/13
# @Author  : Bruce lee
# @function : 输出字符串中包含指定字母的个数


while True:
    try:
        str_input = input().upper()
        str_judge = input().upper()
        print(str_input.count(str_judge))
    except:
        break
