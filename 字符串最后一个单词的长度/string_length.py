# -*- coding: utf-8 -*-
# @Time    : 2020/9/13
# @Author  : Bruce lee
# @function : 输出字符串最后一个单词长度, 空格隔开


def last_string_length(input_str):
    return len(input_str.split(" ")[-1])

while True:
    try:
        print(last_string_length(input()))
    except:
        break
