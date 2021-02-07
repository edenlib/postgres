"""Provides an interactive editing environment.

Python 3.8 @ Eden
Author: Adam Turner <turner.adch@gmail.com>
"""

# standard library
import sys
# eden library
import conndb
# local modules
import yahoo_finance


def update_yahoo():
    yahoo_finance.drop_create_table(curs)
    yahoo_finance.drop_create_staging_table(curs)
    return None


if __name__ == "__main__":
    fpath = sys.argv[1]
    conn = conndb.DBConfig.from_json(fpath).create_psycopg2_connection()

    with conn.cursor() as curs:
        breakpoint()
        print("COMMITTING...")

    conn.commit()

    conn.close()
