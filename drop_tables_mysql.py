"""MySQL database table removal module."""

import mysql.connector
import yaml

def drop_tables():
    """Drops all database tables if they exist."""
    # Load database configuration
    with open('app_config.yml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
        db_config = config['datastore']

    conn = mysql.connector.connect(
        user=db_config['user'],
        password=db_config['password'],
        host=db_config['hostname'],
        port=db_config['port'],
        database=db_config['db']
    )
    c = conn.cursor()

    # Drop air_quality table
    c.execute('''
        DROP TABLE IF EXISTS air_quality
    ''')

    # Drop weather table
    c.execute('''
        DROP TABLE IF EXISTS weather
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    drop_tables()
    print("Database tables dropped successfully.")
