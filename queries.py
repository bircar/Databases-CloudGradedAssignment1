 # This query retrieves all columns from the flight, destination, aircraft, and pilot tables where the destination_id matches the argument provided
def retrieve_flights_by_destination(cursor, destination_id):
    query = """
        SELECT *
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
        print("Destination:", row[4], row[5], "Airport Code:", row[6])
        print("Aircraft:", row[8], row[7], "Capacity:", row[9])
        print("Pilot:", row[10], row[11], "License Number:", row[12], "\n")

# This query adds a new flight to the database using the provided flight data. n.b., the flight_id is auto-incremented, so it does not need to be provided.
def add_new_flight(cursor, flight_data):
    query = """
        INSERT INTO flight (pilot_id, destination_id, aircraft_id)
        VALUES (?, ?, ?)
    """
    cursor.execute(query, flight_data)
    print("New flight added successfully.")

def assign_pilot_to_flight(cursor,