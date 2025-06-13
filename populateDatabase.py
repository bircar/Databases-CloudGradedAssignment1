from sampleData import pilots, destinations, aircrafts, flights
from dbConnection import get_connection

# This function populates the database with the sample data.
def populate_database():
    conn = get_connection()
    #IGNORE is used to prevent duplicate entries in the database, which would cause an error if the same data is inserted again.
    conn.executemany("INSERT OR IGNORE INTO pilot (pilot_id, first_name, last_name, license_number) VALUES (?, ?, ?, ?)", pilots)
    conn.executemany("INSERT OR IGNORE INTO destination (destination_id, city, country, airport_code) VALUES (?, ?, ?, ?)", destinations)
    conn.executemany("INSERT OR IGNORE INTO aircraft (aircraft_id, Airline, model, capacity) VALUES (?, ?, ?, ?)", aircrafts)
    conn.executemany("INSERT OR IGNORE INTO flight (flight_id, pilot_id, destination_id, aircraft_id, departure_date_and_time, arrival_date_and_time, status, origin) VALUES (?, ?, ?, ?, ?, ?, ? ,?)", flights)
    
    conn.commit()
    conn.close()
