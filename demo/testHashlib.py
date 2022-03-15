# /usr/bin/env python3
#! -*- coding:utf-8 -*-
from base64 import encode
import hmac,random

#设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
#将上一节的salt改为标准的hmac算法，验证用户口令：

class User(object):
    def __init__(self, name, passwd) -> None:
        self.name = name
        self.key = "".join(chr(random.randint(48,122)) for i in range(20))
        self.passwd = hmac_md5(self.key,passwd)
        
def hmac_md5(k,s):
    return hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(name, passwd):
    user = db[name]
    return db[name].passwd == hmac_md5(user.key,passwd)
    

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')