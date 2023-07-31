#!/usr/bin/python3
'''script that lists all states from hbtn_0e_0_usa'''
import sys
import MySQLdb


if __name__ == '__main__':

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")

    cur = db.cursor()

    query = " ".join([
        "SELECT * FROM states",
        "WHERE name LIKE BINARY 'N%'",
        "ORDER BY id ASC"])

    cur.execute(query)
    rows = cur.fetchall()

    if not rows:
        print("No matching rows found.")

    for row in rows:
        print(row)

    cur.close()
    db.close()
