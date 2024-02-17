#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa."""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    myQuery = " ".join([
        "SELECT cities.name FROM cities",
        "INNER JOIN states ON states.id = cities.state_id",
        "WHERE states.name = %s",
        "ORDER BY cities.id"
    ])
    cur.execute(myQuery, (sys.argv[4],))
    result = cur.fetchall()
    for row in result:
        print(row[0])
    cur.close()
    db.close()
