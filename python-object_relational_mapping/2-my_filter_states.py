#!/usr/bin/python3
'''script that lists all states from hbtn_0e_0_usa'''
import sys
import MySQLdb


if __name__ == '__main__':

    if len(sys.argv) == 5:
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
            "WHERE name LIKE BINARY '{}'",
            "ORDER BY id ASC"]).format(sys.argv[4])

        cur.execute(query)
        rows = cur.fetchall()

        if not rows:
            print("No matching rows found.")

        for row in rows:
            print(row)

        cur.close()
        db.close()
