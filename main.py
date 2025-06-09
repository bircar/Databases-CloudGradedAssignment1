import sqlite3
from dbConnection import get_connection
from schema import initialiseTables
from populateDatabase import populate_database
from queries import *

conn = get_connection()

print("Database connection established")

initialiseTables(conn)
print ("Table created successfully")

populate_database()
print("Database populated successfully")

cursor = conn.cursor()

print("What would you like to do?")

retrieve_flights_by_destination(cursor, 1)

conn.close
print("Database connection closed")