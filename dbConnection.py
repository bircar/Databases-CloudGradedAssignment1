# This module is responsible for establishing a connection to the SQLite database. 
# It inlcudes error handling to ensure that the connection is successful and returns a connection object.

import sqlite3

def get_connection(db_name='flights'):
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None