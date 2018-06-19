#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb


db = MySQLdb.connect("nap_nm-master.db.tuniu-sst.org","nap_nm_rw","tuniu520","nap_nm")

cursor=db.cursor()
sql="""SELECT notice_content FROM notice WHERE notice_name = "78" """
try:
    cursor.execute(sql)
except:
    db.rollback()
data=cursor.fetchone()
print type(data)
print "The MySQL version is %s" % data
db.close()
