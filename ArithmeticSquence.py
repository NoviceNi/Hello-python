#! /usr/bin/env python3
# -*- coding:utf-8 -*-

def checkIndex(key):
    if not isinstance(key,int):raise TypeError
    if key < 0: raise ValueError

class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        checkIndex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step


    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value


if  __name__ == "__main__":
    aas = ArithmeticSequence(2, 2)
    aas[2] = 5
    print(aas[2])

