#!/usr/bin/python3
"""lists all cities in given state
takes 3 arguments: mysql username, mysql password, db name and state"""

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    state = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=user, passwd=password, db=db, charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                """)
    query_rows = cur.fetchall()

    city = []
    for row in query_rows:
        if row[4] == state:
            city.append(row[2])
    print(", ".join(city))
    cur.close()
    conn.close()
