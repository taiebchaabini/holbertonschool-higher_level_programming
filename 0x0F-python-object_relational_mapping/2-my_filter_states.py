#!/usr/bin/python3
""" script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
from sys import argv
user = argv[1]
pwd = argv[2]
dbname = argv[3]
keyword = argv[4]
query = "SELECT * FROM states WHERE name='"+keyword+"' ORDER BY id"
db = MySQLdb.connect(host="localhost", user=user, passwd=pwd, db=dbname)
cur = db.cursor()
cur.execute(query)
rows = cur.fetchall()
for row in rows:
    print(row)
