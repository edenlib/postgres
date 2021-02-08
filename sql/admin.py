"""Provides an interactive SQL environment.

Python 3.8 @ Eden
Author: Adam Turner <turner.adch@gmail.com>
"""

# standard library
import sys
# eden library
import conndb

if __name__ == "__main__":
    fpath = sys.argv[1]

    conn = conndb.DBConfig.from_json(fpath).create_psycopg2_connection()

    with conn.cursor() as curs:
        breakpoint()
        print("COMMIT!")

    conn.commit()

    conn.close()
