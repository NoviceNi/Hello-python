#! /usr/bin/env python
# -*- coding:utf-8 -*-
import functools
import time

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("Begin to call %s at %s " % (func.__name__, time.time()))
        x = func(*args, **kw)
        print("end to call %s at %s " % (func.__name__, time.time()))
        return x
    return wrapper

def log2(*test):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if test.__len__():
                print ("%s Run log2" % test[0])
            else:
                print ("admin Run log2")
            return func(*args, **kw)
        return wrapper
    return decorator

@log2("Jhon")
def test():
    print ('run test()')

test()