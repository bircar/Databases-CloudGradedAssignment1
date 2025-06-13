# This module is responsible for establishing a connection to the SQLite database. 

import sqlite3
def get_connection(db_name='flights'):
    return sqlite3.connect(db_name)