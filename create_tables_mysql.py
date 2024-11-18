"""MySQL database table creation module."""

import mysql.connector
import yaml

def create_tables():
    """Creates the required database tables if they don't exist."""
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

    # Create air_quality table
    c.execute('''
        CREATE TABLE IF NOT EXISTS air_quality
        (id INT AUTO_INCREMENT PRIMARY KEY,
         reading_id VARCHAR(36) NOT NULL,
         sensor_id VARCHAR(250) NOT NULL,
         timestamp VARCHAR(100) NOT NULL,
         pm2_5_concentration FLOAT NOT NULL,
         pm10_concentration FLOAT NOT NULL,
         co2_level FLOAT NOT NULL,
         o3_level FLOAT NOT NULL,
         date_created VARCHAR(100) NOT NULL,
         trace_id VARCHAR(36) NOT NULL)
    ''')

    # Create weather table
    c.execute('''
        CREATE TABLE IF NOT EXISTS weather
        (id INT AUTO_INCREMENT PRIMARY KEY,
         reading_id VARCHAR(36) NOT NULL,
         sensor_id VARCHAR(250) NOT NULL,
         timestamp VARCHAR(100) NOT NULL,
         temperature FLOAT NOT NULL,
         humidity FLOAT NOT NULL,
         wind_speed FLOAT NOT NULL,
         noise_level FLOAT NOT NULL,
         date_created VARCHAR(100) NOT NULL,
         trace_id VARCHAR(36) NOT NULL)
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    print("Database tables created successfully.")
