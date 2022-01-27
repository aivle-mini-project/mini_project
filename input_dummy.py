# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 21:56:01 2020
@author: 82108
"""
import pandas as pd
import numpy as np
import random
import math
import sqlite3
from random import randint,randrange,choices
import datetime as dt
import json

def random_date(year,month,day):#     
    hour=randint(7,23)
    minute=randint(0,59)
    mk_date=dt.datetime(year,month,day,hour,minute).strftime("%Y-%m-%d %H:%M")

    return mk_date
user_list = [0]*5
user_list[0] = '123456'  #password
user_list[1] = 'user_last'+str(1)+'@aivle.com'#id
user_list[2] = random_date(2021,3,13)
user_list[3] = 'user_last'+str(1)
user_list[4] = ''

conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()
##t시작
sql = "insert into Emotics_user(password,email,register_date,username,profile_img) values ('"+user_list[0]+"','"+user_list[1]+"','"+user_list[2]+"','"+user_list[3]+"','"+user_list[4]+"');"
c.execute(sql)
conn.commit()
#####dictionary 불러오는 부분)
day = 0
sql11=''
for idx in range(3):#일이 바뀌는 부분
    sql1 ='(select id from Emotics_user where username = "'+user_list[3]+'")'
    day +=(1+randint(0,2))
    with open('./result/result'+str(idx+20)+'.json', 'r') as f:
        result = json.load(f)
    #####diary
    full_text =''
    for i in result["sentences"]:
        full_text+= i['content']
    print(full_text)
    user_list_d = [0]*7
    user_list_d[1] = full_text
    user_list_d[2] = result['document']['sentiment']
    user_list_d[3] = str(result['document']['confidence']['neutral'])
    user_list_d[4] = str(result['document']['confidence']['positive'])
    user_list_d[5] = str(result['document']['confidence']['negative'])
    user_list_d[6] = random_date(2021,5,day)
    sql11 ="insert into diary(writer_id,write,emotion,neutral,positive,negative,register_date) values ("+sql1+",'"+user_list_d[1]+"','"+user_list_d[2]+"',"+user_list_d[3]+","+user_list_d[4]+","+user_list_d[5]+",'"+user_list_d[6]+"');"
    c.execute(sql11)
    conn.commit()
    sql22 =''
    #######diary_detail
    for sentence in result["sentences"]:
        sql2 ='(select id from diary where write = "'+user_list_d[1]+'")'
        user_list_dt = [0]*6
        user_list_dt[1] = sentence['content']
        user_list_dt[2] = sentence['sentiment']
        user_list_dt[3] = str(sentence['confidence']['neutral'])
        user_list_dt[4] = str(sentence['confidence']['positive'])
        user_list_dt[5] = str(sentence['confidence']['negative'])
        sql22 ="insert into diary_detail(diary_id,write,emotion,neutral,positive,negative) values ("+sql2+",'"+user_list_dt[1]+"','"+user_list_dt[2]+"',"+user_list_dt[3]+","+user_list_dt[4]+","+user_list_dt[5]+");"
        c.execute(sql22)
        conn.commit()
        sql3=''
        #########diary_detail_highlights
        for highlight in sentence['highlights']:
            sql3 ='(select id from diary_detail where write = "'+user_list_dt[1]+'")'
            user_list_dth = [0]*3
            user_list_dth[1] = str(highlight['offset'])
            user_list_dth[2] = str(highlight['length'])
            sql33 ="insert into diary_detail_highlight(diary_detail_id,offset,length) values ("+sql3+","+user_list_dth[1]+","+user_list_dth[2]+");"
            c.execute(sql33)
            conn.commit()

c.close()

