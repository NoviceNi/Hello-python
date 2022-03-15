# -*- coding:utf-8 -*-
from audioop import reverse
from functools import reduce

def str2float(str):
    s = str.split(".")

    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,'5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def str2num(s):
        return digits[s]

    def n1(x,y):
        return x*10 + y
        
    return reduce(n1,map(str2num,s[0])) + reduce(n1,map(str2num,s[1]))*0.1**len(s[1])


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
