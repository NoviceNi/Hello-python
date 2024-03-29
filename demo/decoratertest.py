# -*- coding:utf-8 -*-
#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：


import functools,time
from tracemalloc import start


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        starttime = time.time()
        fn_value = fn(*args,**kw)
        endtime = time.time()
        print('%s executed in %s ms, fn_value is %d' % (fn.__name__, endtime - starttime,fn_value))
        return fn_value
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')