# This module is responsible for establishing a connection to the SQLite database. 

def get_connection(db_name='flights'):
    return sqlite3.connect(db_name)