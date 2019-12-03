#!/usr/bin/env python3
# -*- coding utf-8 -*-

'''
利用闭包返回一个计数器函数，每次调用它返回递增整数
'''

def createCounter():
    def auto_add():
        n = 0
        while True:
            n = n + 1
            yield n
    
    x = auto_add()

    def counter():
        return next(x)
            
    return counter



if __name__ == "__main__":
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')