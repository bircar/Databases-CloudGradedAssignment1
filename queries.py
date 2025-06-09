def retrieve_flights_by_destination(cursor, destinationID):
    cursor.execute("SELECT * FROM flight WHERE destination_id = ?", (destinationID,))
    for row in cursor.fetchall():
        print(row)