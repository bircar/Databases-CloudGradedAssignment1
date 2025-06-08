# This function creates the tables for the database if they do not already exist.
def initialiseTables(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS pilot (
            PilotID INTEGER PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            license_number VARCHAR(5)
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS destination (
            DestinationID INTEGER PRIMARY KEY,
            city VARCHAR(100),
            country VARCHAR(100),
            airport_code VARCHAR(3)
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS aircraft (
            AircraftID INTEGER PRIMARY KEY,
            Airline VARCHAR(50),
            model VARCHAR(100),
            capacity INTEGER
        )
    """)

# Foreign keys are used to link the flight table to the pilot, destination, and aircraft tables, prevnting invalid data entries.
    conn.execute("""
        CREATE TABLE IF NOT EXISTS flight (
            FlightID INTEGER PRIMARY KEY,
            pilot_id INTEGER NOT NULL,
            destination_id INTEGER NOT NULL,
            aircraft_id INTEGER,
            FOREIGN KEY (pilot_id) REFERENCES pilot(PilotID),                   
            FOREIGN KEY (destination_id) REFERENCES destination(DestinationID),
            FOREIGN KEY (aircraft_id) REFERENCES aircraft(AircraftID)
        )
    """)
