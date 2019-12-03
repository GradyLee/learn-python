#!/usr/bin/env python3
# -*- coding utf-8 -*-

'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
'''


def normalize(name):
    if len(name) == 0:
        return None
    s = str.upper(name[0]) + "".join(list(map(str.lower, name[1:]))) 
    return s
    '''
    return s.capitalize(name)
    '''
    
    

if __name__ == "__main__":
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)