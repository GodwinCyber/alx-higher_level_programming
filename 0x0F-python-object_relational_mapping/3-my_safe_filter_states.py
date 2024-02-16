#!/usr/bin/python3
""" Takes in an argument and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument
    (safe from MySQL injection)
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

cur = db.cursor()
search = sys.argv[4].encode("utf8")
cur.execute("SELECT * FROM states WHERE name = %s \
                ORDER BY id ASC", (search,))
result = cur.fetchall()
for row in result:
    print(row)
cur.close()
db.close()
