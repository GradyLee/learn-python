#!/usr/bin/env python3
# -*- coding utf-8 -*-

'''
设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
'''
class Screen(object):
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        return self.__height * self.__width

if __name__ == "__main__":
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')