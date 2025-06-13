# This file contains the SQL queries used to interact with the database. Each function corresponds to a specific query and handles the retrieval or modification of 
# data in the database and prints the results in a user-friendly format.


# This query retrieves flights based on specified criteria such as destination, airline, or departure date, ordered by departure date and time.
def retrieve_flights_by_criteria(cursor, criteria_and_value):
    
    # Map user input search field to actual DB columns
    criteria_map = {
        'destination': 'destination.airport_code',
        'origin': 'flight.origin',
        'airline': 'aircraft.Airline',
        'departure_date': 'flight.departure_date_and_time',
    }

    db_criteria = criteria_map[criteria_and_value[0]]
    # Check if the criteria has been input correctly by checking if the key exists in the criteria_map
    if not db_criteria:
        print(f"Invalid criteria: {criteria_and_value[0]}")
        return
    # If searching by departure_date, use SQLite's strftime to match only the date part
    if criteria_and_value[0] == 'departure_date':
        query = f"""
            SELECT flight.flight_id, flight.departure_date_and_time, flight.arrival_date_and_time, destination.city, destination.country, destination.airport_code,
                   aircraft.model, aircraft.Airline, aircraft.capacity,
                   pilot.first_name, pilot.last_name,
                   flight.status, flight.origin
            FROM flight
            NATURAL JOIN destination
            NATURAL JOIN aircraft
            NATURAL JOIN pilot
            WHERE strftime('%Y-%m-%d', flight.departure_date_and_time) = ?
            GROUP BY departure_date_and_time
        """
        cursor.execute(query, (criteria_and_value[1],))
    else:
        query = f"""
            SELECT flight.flight_id, flight.departure_date_and_time, flight.arrival_date_and_time, destination.city, destination.country, destination.airport_code,
                   aircraft.model, aircraft.Airline, aircraft.capacity,
                   pilot.first_name, pilot.last_name,
                   flight.status, flight.origin
            FROM flight
            NATURAL JOIN destination
            NATURAL JOIN aircraft
            NATURAL JOIN pilot
            WHERE {db_criteria} = ?
            GROUP BY departure_date_and_time
        """
        cursor.execute(query, (criteria_and_value[1],))
    results = cursor.fetchall()
    if results:
        for row in results:
            print("\nFlight ID:", row[0])
            print("Departure Time:", row[1], "Arrival Time:", row[2])
            print("Destination:", row[3], row[4], "Airport Code:", row[5])
            print("Aircraft:", row[6], row[7], "Capacity:", row[8])
            print("Pilot:", row[9], row[10])
            print("Status:", row[11], "Origin:", row[12], "\n")
    else:
        print("\nNo flights found for the given criteria.")

# This query adds a new flight to the database using the provided flight data. n.b., the flight_id is auto-incremented, so it does not need to be provided.
def add_new_flight(cursor, flight_data):
    query = """
        INSERT INTO flight (pilot_id, destination_id, aircraft_id)
        VALUES (?, ?, ?)
    """
    cursor.execute(query, flight_data)
    print("\nNew flight added successfully.")

# This query assigns a pilot to a flight by updating the pilot_id in the flight table for the specified flight_id.
def assign_pilot_to_flight(cursor, pilot_and_flight_id):
    query = """
        UPDATE flight
        SET pilot_id = ?
        WHERE flight_id = ?
    """
    cursor.execute(query, pilot_and_flight_id)
    print("\nPilot assigned to flight successfully.")

# This query displays the schedule for a specific pilot based on their ID, ordered by departure date.
def view_pilot_schedule(cursor, pilot_id):
    query = """
        SELECT flight.flight_id, flight.departure_date_and_time, destination.city, destination.country, destination.airport_code,
               aircraft.model, aircraft.Airline, aircraft.capacity,
               pilot.first_name, pilot.last_name,
               flight.status, flight.origin
        FROM flight
        NATURAL JOIN destination
        NATURAL JOIN aircraft
        NATURAL JOIN pilot
        WHERE pilot_id = ?
        GROUP BY flight.departure_date_and_time
    """
    cursor.execute(query, pilot_id)
    flights = cursor.fetchall()
    
    if flights:
        print(f"Schedule for Pilot ID {pilot_id}:")
        for row in flights:
            print("Flight ID:", row[0])
            print("Departure Time:", row[1])
            print("Destination:", row[2], row[3], "Airport Code:", row[4])
            print("Aircraft:", row[5], row[6], "Capacity:", row[7])
            print("Pilot:", row[8], row[9])
            print("Status:", row[10], "Origin:", row[11], "\n")                     
    else:
        print(f"\nNo flights found for Pilot ID {pilot_id}.")

# This query retrieves flights scheduled between the two specified date/time values, ordered by earliest departure time.
def retrieve_departures_between_datetimes(cursor, start_and_end_datetimes):
    query = """
            SELECT flight.flight_id, flight.departure_date_and_time, destination.city, destination.country, destination.airport_code,
                   aircraft.model, aircraft.Airline, aircraft.capacity,
                   pilot.first_name, pilot.last_name,
                   flight.status, flight.origin
            FROM flight
            NATURAL JOIN destination
            NATURAL JOIN aircraft
            NATURAL JOIN pilot
            WHERE departure_date_and_time BETWEEN ? AND ?
            GROUP BY departure_date_and_time
        """
    cursor.execute(query, start_and_end_datetimes)
    flights = cursor.fetchall()
        
    if flights:
            for row in flights:
                print("Flight ID:", row[0])
                print("Departure Time:", row[1])
                print("Destination:", row[2], row[3], "Airport Code:", row[4])
                print("Aircraft:", row[5], row[6], "Capacity:", row[7])                 
                print("Pilot:", row[8], row[9])
                print("Status:", row[10], "Origin:", row[11], "\n")
    else:
            print("\nNo flights found in the specified date range.")

# This query retrieves fligths scheduled to arrive bettwen two specified date/time values, ordered by earliest arrival time.
def retrieve_arrivals_between_datetimes(cursor, start_and_end_datetimes):
    query = """
            SELECT flight.flight_id, flight.arrival_date_and_time, destination.city, destination.country, destination.airport_code,
                   aircraft.model, aircraft.Airline, aircraft.capacity,
                   pilot.first_name, pilot.last_name,
                   flight.status, flight.origin
            FROM flight
            NATURAL JOIN destination
            NATURAL JOIN aircraft
            NATURAL JOIN pilot
            WHERE arrival_date_and_time BETWEEN ? AND ?
            GROUP BY arrival_date_and_time
        """
    cursor.execute(query, start_and_end_datetimes)
    flights = cursor.fetchall()
        
    if flights:
            for row in flights:
                print("Flight ID:", row[0])
                print("Arrival Time:", row[1])
                print("Destination:", row[2], row[3], "Airport Code:", row[4])
                print("Aircraft:", row[5], row[6], "Capacity:", row[7])                 
                print("Pilot:", row[8], row[9])
                print("Status:", row[10], "Origin:", row[11], "\n")
    else:
            print("\nNo flights found in the specified date range.")

def update_flight_schedule(cursor, flight_data):
    # Flight data will be input by the user in the wrong order for the update query, so we need to rearrange it.
    flight_id, departure_date, arrival_date, status = flight_data
    query_values = (departure_date, arrival_date, status, flight_id)
    query = """
        UPDATE flight
        SET departure_date_and_time = ?, arrival_date_and_time = ?, status = ?
        WHERE flight_id = ?
    """
    cursor.execute(query, query_values)
    print("\nFlight schedule updated successfully.")

# This query deletes a flight from the database based on the provided flight_id.
def delete_flight(cursor, flight_id):
    query = """
        DELETE FROM flight
        WHERE flight_id = ?
    """
    cursor.execute(query, flight_id)
    print("\nFlight deleted successfully.")

# This query simply returns all flights in the database, ordered by departure date and time.
def view_all_flights(cursor, placeholder): # Placeholder is requir to match required arguments for the query handler
    query = """
        SELECT *
        FROM flight
        ORDER BY flight.departure_date_and_time
    """
    cursor.execute(query)
    flights = cursor.fetchall()

    if flights:
        for row in flights:
            print("Flight ID:", row[0])
            print("Pilot ID:", row[1])
            print("Destination ID:", row[2])
            print("Aircraft ID:", row[3])
            print("Departure Date and Time:", row[4])
            print("Arrival Date and Time:", row[5])
            print("Status:", row[6])
            print("Origin:", row[7], "\n")
    else:
        print("\nNo flights found in the database.")

# This function counts the number of flights in the database that match the specified criteria, such as destination, origin, airline, or departure date.
def count_flights_by_criteria(cursor, criteria_and_value):
    # Map user input search field to actual DB columns
    criteria_map = {
        'destination': 'destination.airport_code',
        'origin': 'flight.origin',
        'airline': 'aircraft.Airline',
        'departure_date': 'flight.departure_date_and_time',
    }

    db_criteria = criteria_map[criteria_and_value[0]]
    if not db_criteria:
        print(f"Invalid criteria: {criteria_and_value[0]}")
        return

    if criteria_and_value[0] == 'departure_date':
        query = f"""
            SELECT COUNT(*)
            FROM flight
            NATURAL JOIN destination
            NATURAL JOIN aircraft
            NATURAL JOIN pilot
            WHERE strftime('%Y-%m-%d', flight.departure_date_and_time) = ?
        """
        cursor.execute(query, (criteria_and_value[1],))
    else:
        query = f"""
            SELECT COUNT(*)
            FROM flight
            NATURAL JOIN destination
            NATURAL JOIN aircraft
            NATURAL JOIN pilot
            WHERE {db_criteria} = ?
        """
        cursor.execute(query, (criteria_and_value[1],))
    
    count = cursor.fetchone()[0]
    print(f"\nNumber of flights matching the criteria '{criteria_and_value[0]}': {count}")