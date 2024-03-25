#!/usr/bin/python3
"""lists all states starting with N
takes 3 arguments: mysql username, mysql password and database name
"""

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=user, passwd=password, db=db, charset="utf8")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name like 'N%' ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
