#! /usr/bin/env python
from re import A


# -*- coding:utf-8 -*-

print("Hello,world")

def mul(*num):
    if not isinstance(num,(int,float,tuple)) or num == ():
        raise TypeError("bad opread type")
    else:
        res=1
        for n in num:
            res = res*n
        return res


# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')