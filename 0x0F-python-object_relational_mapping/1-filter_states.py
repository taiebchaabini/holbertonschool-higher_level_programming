#!/usr/bin/python3
""" script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa """
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]
    db = MySQLdb.connect(host="localhost", user=user, passwd=pwd, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
