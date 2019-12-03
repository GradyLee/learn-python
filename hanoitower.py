#!/usr/bin/env python3
# -*- coding utf-8 -*-



'''
汉诺塔游戏递归解法
'''

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

if __name__ == "__main__":
    move(6, 'A', 'B', 'C')