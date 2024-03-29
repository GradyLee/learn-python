#!/usr/bin/env python3
# -*- coding utf-8 -*-



'''
求解一元二次方程ax2+bx+c=0的解
'''

import math

def quadratic(a, b, c):
    t = math.sqrt(b * b - 4 * a * c)
    x1 = (-b + t) / (2 * a)
    x2 = (-b - t) / (2 * a)
    return x1, x2


if __name__ == "__main__":
	print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
	print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

	if quadratic(2, 3, 1) != (-0.5, -1.0):
		print('测试失败')
	elif quadratic(1, 3, -4) != (1.0, -4.0):
		print('测试失败')
	else:
		print('测试成功')