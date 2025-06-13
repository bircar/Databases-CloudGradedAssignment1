# This is the main file that runs the program - it calls other functions to initialise the database, populate it with the sample data, and allows the user to interact with the database via the command line.

import sqlite3
from dbConnection import get_connection
from schema import initialiseTables
from populateDatabase import populate_database
from queries import *
from queryHandler import *

conn = get_connection()
print("Database connection established")

initialiseTables(conn)
print ("Table created successfully")

populate_database()
print("Database populated successfully")

# Get cursor to execute queries
cursor = conn.cursor()

# Flag to control the menu loop
is_menu_active = True
print("\nWelcome to the Flight Management System!")

while is_menu_active:
    input_choice = input("""\nWhat would you like to do? Enter the number of the action you want to perform:\n
    1 : Retrieve flights by criteria:
    2 : Add a new flight:
    3 : Assign a pilot to a flight:
    4 : View a pilot's schedule:
    5 : View all flights departing within time period:
    6 : View all flights arriving within time period:                    
    7 : Update flight schedule:
    8 : Delete a flight:
    9 : View all flights:
    10 : Retrieve number of flights by criteria:
    
    Type 'x' to close.\n""")
    if input_choice == "x":
        print("Exiting the program")
        is_menu_active = False
        break

    selected_query = handle_query(input_choice)
    # The query handler module returns the function corresponding to the user's input, or None if the choice is invalid.
    if selected_query is None:
        continue

    # If the selected query is valid, get the required criteria from the user
    criteria = get_criteria(input_choice)

    # Execute the selected query with the provided criteria
    selected_query(cursor, criteria)
    
    # Commit the changes to the database after successful execution of the query
    conn.commit()
    continue

# Close the cursor and database connection
cursor.close()
conn.close()
print("Database connection closed")