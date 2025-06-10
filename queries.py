# This file contains the SQL queries used to interact with the database. Each function corresponds to a specific query and handles the retrieval or modification of 
# data in the database and prints the results in a user-friendly format.


# This query retrieves all columns from the flight, destination, aircraft, and pilot tables where the destination_id matches the argument provided
def retrieve_flights_by_destination(cursor, destination_id):
    query = """
        SELECT flight.flight_id, destination.city, destination.country, destination.airport_code,
               aircraft.model, aircraft.manufacturer, aircraft.capacity,
               pilot.first_name, pilot.last_name, pilot.license_number
        FROM flight
        NATURAL JOIN destination
        NATURAL JOIN aircraft
        NATURAL JOIN pilot
        WHERE destination_id = ?
    """
    cursor.execute(query, destination_id)
    # Skip primary keys to only provide user friendly information
    for row in cursor.fetchall():
        print("Flight ID:", row[0])
        print("Destination:", row[1], row[2], "Airport Code:", row[3])
        print("Aircraft:", row[4], row[5], "Capacity:", row[6])
        print("Pilot:", row[7], row[8], "License Number:", row[9], "\n")

# This query adds a new flight to the database using the provided flight data. n.b., the flight_id is auto-incremented, so it does not need to be provided.
def add_new_flight(cursor, flight_data):
    query = """
        INSERT INTO flight (pilot_id, destination_id, aircraft_id)
        VALUES (?, ?, ?)
    """
    cursor.execute(query, flight_data)
    print("New flight added successfully.")

# This query assigns a pilot to a flight by updating the pilot_id in the flight table for the specified flight_id.
def assign_pilot_to_flight(cursor, pilot_and_flight_id):
    query = """
        UPDATE flight
        SET pilot_id = ?
        WHERE flight_id = ?
    """
    cursor.execute(query, pilot_and_flight_id)
    print("Pilot assigned to flight successfully.")

# This query displays the schedule for a specific pilot based on their ID.
def view_pilot_schedule(cursor, pilot_id):
    query = """
        SELECT flight.flight_id, destination.city, destination.country, destination.airport_code,
               aircraft.model, aircraft.manufacturer, aircraft.capacity,
               pilot.first_name, pilot.last_name, pilot.license_number
        FROM flight
        NATURAL JOIN destination
        NATURAL JOIN aircraft
        NATURAL JOIN pilot
        WHERE pilot_id = ?
    """
    cursor.execute(query, pilot_id)
    flights = cursor.fetchall()
    
    if flights:
        print(f"Schedule for Pilot ID {pilot_id}:")
        for row in flights:
            print("Flight ID:", row[0])
            print("Destination:", row[1], row[2], "Airport Code:", row[3])
            print("Aircraft:", row[4], row[5], "Capacity:", row[6])
            print("Pilot:", row[7], row[8], "License Number:", row[9], "\n")
    else:
        print(f"No flights found for Pilot ID {pilot_id}.")