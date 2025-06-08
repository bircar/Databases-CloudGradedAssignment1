from sampleData import pilots, destinations, aircrafts, flights
from dbConnection import get_connection

# This function populates the database with thw sample data.
def populate_database():
    conn = get_connection()
    
    conn.executemany("INSERT INTO pilot (PilotID, first_name, last_name, license_number) VALUES (?, ?, ?, ?)", pilots)
    conn.executemany("INSERT INTO destination (DestinationID, city, country, airport_code) VALUES (?, ?, ?, ?)", destinations)
    conn.executemany("INSERT INTO aircraft (AircraftID, Airline, model, capacity) VALUES (?, ?, ?, ?)", aircrafts)
    conn.executemany("INSERT INTO flight (FlightID, pilot_id, destination_id, aircraft_id) VALUES (?, ?, ?, ?)", flights)
    
    conn.commit()
    print("Database populated successfully")
    
    conn.close()
