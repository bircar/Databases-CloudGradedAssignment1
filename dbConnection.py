import sqlite3

# Try/catch block to handle potential errors??
def get_connection(db_name="flights"):
    return sqlite3.connect(db_name)