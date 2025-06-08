import sqlite3
from dbConnection import get_connection
from schema import create_tables
from populateDatabase import populate_database

conn = get_connection()

print("Database connection established")

create_tables(conn)
print ("Table created successfully")


conn.close
print("Database connection closed")