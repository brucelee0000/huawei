# -*- coding: utf-8 -*-
# @Time    : 2020/9/13
# @Author  : Bruce lee
# @function : 对输入的多组整数去重排序

import sys


while True:
    try:
        input_line = sys.stdin.readline()
        if not input_line:
            break
        out_array = []
        for i in range(int(input_line)):
            each_out = sys.stdin.readline()
            out_array.append(int(each_out))

        out_array = list(set(out_array))
        out_array.sort()
        for i in out_array:
            print(i)
    except:
        break
