#!/usr/bin/env python3
# -*- coding utf-8 -*-

'''
使用迭代查找一个list中最小和最大值
'''

def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    h=L[0]
    l=L[0]
    for i in L:
        if (i >= h):
            h = i
        if (i <= l):
            l = i
    return (l, h)
    
    

if __name__ == "__main__":
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')