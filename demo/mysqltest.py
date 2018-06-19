#! /usr/bin/env python
# -*- coding:utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(user='root', password='Tuniu520', database='test')
cursor = conn.cursor()

sql = """create table if not exists user(
id INT unsigned auto_increment comment '用户ID',
username VARCHAR (20) not NULL comment '用户姓名',
sex TINYINT comment '性别，0：女，1：男',
age INT UNSIGNED,
 PRIMARY KEY(id)
 )ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
try:
    cursor.execute(sql)
except:
    print("CREATE table failed!")

sql2 = """insert into USER (username, sex, age) VALUES ("临安", 1, 15)"""

try:
    cursor.execute(sql2)
except:
    print("Insert data failed!")

conn.commit()
cursor.close()
