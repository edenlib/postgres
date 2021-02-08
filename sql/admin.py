"""Provides an interactive SQL environment.

Python 3.8 @ Eden
Author: Adam Turner <turner.adch@gmail.com>
"""

# standard library
import sys
# eden library
import conndb

if __name__ == "__main__":
    # database config json file path
    cfgpath = sys.argv[1]
    # sql code file path
    sqlpath = sys.argv[2]

    conn = conndb.DBConfig.from_json(cfgpath).create_psycopg2_connection()

    try:
        with conn.cursor() as curs:
            with open(sqlpath, "r") as sql:
                curs.execute(sql.read())
        conn.commit()
    finally:
        conn.close()
