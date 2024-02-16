#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa
   take 3 arguments: mysql username, mysql password and database name
   You must use the module MySQLdb (import MySQLdb)
   connect to a MySQL server running on localhost at port 3306
   sorted in ascending order by states.id
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id")

result = cur.fetchall()
for row in result:
    print(row)

cur.close()
db.close()
