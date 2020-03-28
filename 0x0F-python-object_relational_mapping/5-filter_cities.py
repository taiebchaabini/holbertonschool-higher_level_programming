#!/usr/bin/python3
""" script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa """
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]
    statename = argv[4]
    db = MySQLdb.connect(host="localhost", user=user, passwd=pwd, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT cities.name\
            FROM states INNER JOIN cities ON\
            states.name = '{}' AND\
            states.id = cities.state_id ORDER BY cities.id".format(statename))
    rows = cur.fetchall()
    for col in range(len(rows)):
        print(rows[col][0], end='')
        if (rows[col] != rows[len(rows) - 1]):
            print(", ", end="")
        else:
            print("")
    db.close()
