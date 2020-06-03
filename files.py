import os
'''
import MySQLdb
import csv
#a=os.getcwd()
#b=os.path.join(a,'data')
#c=os.chdir(b)
#d=open('sample.csv','w')

import MySQLdb

db = MySQLdb.connect(host="localhost",
                 user="root",
                 password="root",
                 db="data_dump")
cursor = db.cursor()
a=os.getcwd()
b=os.path.join(a,'data')
c=os.chdir(b)
with open('dump1.txt','r') as f:
    for x in f:
        m,n,o,p,q,r=x.split()
        cursor.execute("insert into insurance_data  values(%s,%s,%s,%s,%s,%s)",(m,n,o,p,q,r))
        db.commit()


import pandas as pd
from pandas.io import sql
import MySQLdb

db = MySQLdb.connect(host="localhost",
                 user="root",
                 password="root",
                 db="data_dump")
cursor = db.cursor()

a=os.getcwd()
b=os.path.join(a,'data')
c=os.chdir(b)
df = pd.read_csv('dump.csv')
for x in df.values:
    m,n,o,p,q,r=x
    cursor.execute("insert into insurance_data  values(%s,%s,%s,%s,%s,%s)", (m, n, o, p, q, r))
    db.commit()
print('data is saved to database')
'''

# Sorting data some fields

import pandas as pd
from pandas.io import sql
import MySQLdb

db = MySQLdb.connect(host="localhost",
                 user="root",
                 password="root",
                 db="data_dump")
cursor = db.cursor()
a=os.getcwd()
b=os.path.join(a,'data')
c=os.chdir(b)
df = pd.read_csv('dump.csv')
for x in df.values:
    m,n,o,p,q,r=x
    cursor.execute("insert into emp  values(%s,%s)", ( n, r))
    db.commit()
print('data is saved to database')

# df.to_sql(con=db,name='insurance_data',index=False,if_exists='append')
# print(df)

