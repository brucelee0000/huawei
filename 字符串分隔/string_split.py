# -*- coding: utf-8 -*-
# @Time    : 2020/9/13
# @Author  : Bruce lee
# @function : 字符串每8位输出，最后不够位数补0


while True:
    try:
        str_input = input()
        length = len(str_input)
        remainder = 8 - length % 8
        if remainder != 8:
            str_input = str_input + "0"*remainder
        if length == 8:
            print(str_input)
        else:
            for i in range(int(len(str_input)/8)):
                print(str_input[i*8:(i+1)*8])
    except:
        break
