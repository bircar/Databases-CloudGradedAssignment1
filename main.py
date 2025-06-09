import sqlite3
from dbConnection import get_connection
from schema import initialiseTables
from populateDatabase import populate_database

conn = get_connection("flights")

print("Database connection established")

initialiseTables(conn)
print ("Table created successfully")

populate_database()
print("Database populated successfully")


conn.close
print("Database connection closed")