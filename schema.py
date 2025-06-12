# This function creates the tables for the database if they do not already exist.
def initialiseTables(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS pilot (
            pilot_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            license_number VARCHAR(5)
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS destination (
            destination_id INTEGER PRIMARY KEY AUTOINCREMENT,
            city VARCHAR(100),
            country VARCHAR(100),
            airport_code VARCHAR(3)
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS aircraft (
            aircraft_id INTEGER PRIMARY KEY AUTOINCREMENT,
            Airline VARCHAR(50),
            model VARCHAR(100),
            capacity INTEGER
        )
    """)

# Foreign keys are used to link the flight table to the pilot, destination, and aircraft tables, prevnting invalid data entries.
    conn.execute("""
        CREATE TABLE IF NOT EXISTS flight (
            flight_id INTEGER PRIMARY KEY AUTOINCREMENT,
            pilot_id INTEGER NOT NULL,
            destination_id INTEGER NOT NULL,
            aircraft_id INTEGER,
            departure_date_and_time TEXT,
            arrival_date_and_time TEXT,
            status VARCHAR(20),
            origin VARCHAR(3),
            FOREIGN KEY (pilot_id) REFERENCES pilot(pilot_id),                   
            FOREIGN KEY (destination_id) REFERENCES destination(destination_id),
            FOREIGN KEY (aircraft_id) REFERENCES aircraft(aircraft_id)
        )
    """)
