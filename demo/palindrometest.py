# -*- coding:utf-8 -*-

from operator import truediv
from tkinter import N


def num():
    n = 10
    while True:
        n = n+1
        yield n


def is_palindrome(i):
    return i and str(i) == str(i)[::-1]


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
    



#
# 
# print(str(123)[::-1])