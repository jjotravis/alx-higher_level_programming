#!/usr/bin/python3
"""lists given states
Takes 3 arguments: username, password, db_name, state_name """

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    filter = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost", port=3306, user=user,
        passwd=password, db=db, charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name like '{}'
                ORDER BY id""".format(filter))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
