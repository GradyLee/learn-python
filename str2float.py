#!/usr/bin/env python3
# -*- coding utf-8 -*-

'''
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
'''

from functools import reduce

def str2float(s):
    digit = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}

    return reduce(lambda x, y: x * 10 + y, map(lambda a : digit[a], s[0:s.index('.')]))   \
            + 0.1 * reduce(lambda x, y: x * 0.1 + y, map(lambda a : digit[a],s[-1:s.index('.'):-1]))
    

if __name__ == "__main__":
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')