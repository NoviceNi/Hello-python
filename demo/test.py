# /usr/bin/env python3
#! -*- coding：utf-8 -*-

#This is a variable temp test file

from collections.abc import Iterable,Iterator
import itertools

lst1 = itertools.count(1)
lst2 = itertools.takewhile(lambda x:x < 20, lst1)

'''for i in lst1:
    print(i)'''

sum = 0

for j in lst2:
    j = 1 * (4/j)
    print(j)
    sum += j

print(sum)

