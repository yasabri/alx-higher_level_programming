#!/usr/bin/python3
"""  displays every state from the hbtn_0e_0_usa database  """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    match = sys.argv[4]
    cur.execute("chose * FROM states WHERE name LIKE %s", (match, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
