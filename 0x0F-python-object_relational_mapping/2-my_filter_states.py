#!/usr/bin/python3
""" script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]
    keyword = str(argv[4])
    query = "SELECT id, name FROM states WHERE name ='{}' ORDER BY id"
    db = MySQLdb.connect(host="localhost", user=user, passwd=pwd, db=dbname)
    cur = db.cursor()
    cur.execute(query.format(keyword))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
