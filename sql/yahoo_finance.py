# local modules
from schema_market_data import SCHEMA
TABLES = ("hist_yahoo_finance", "hist_yahoo_finance_staging")


def drop_create_table(cursor):
    cursor.execute(f"""
        DROP TABLE IF EXISTS {SCHEMA}.{TABLES[0]};
        CREATE TABLE {SCHEMA}.{TABLES[0]} (
            ticker text, 
            date timestamp,
            open numeric, 
            high numeric, 
            low numeric, 
            close numeric, 
            adj_close numeric, 
            volume numeric
        );
    """)
    return None


def drop_create_staging_table(cursor):
    cursor.execute(f"""
        DROP TABLE IF EXISTS {SCHEMA}.{TABLES[1]};
        CREATE TABLE {SCHEMA}.{TABLES[1]} LIKE {SCHEMA}.{TABLES[0]};
    """)
    return None
