SCHEMA = "market_data"


def create_schema(cursor):
    """Holds all kinds of market data."""
    cursor.execute(f"CREATE SCHEMA {SCHEMA};")
    return None
