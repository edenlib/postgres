def create_database(cursor):
    """Creates the database back-end for Airflow."""
    query = """
        create database airflow;
        create user airflow with password 'airflow';
        grant all privileges on database airflow to airflow;
    """
    cursor.execute(query)
    return None
