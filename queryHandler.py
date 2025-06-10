# This file retrieves the correct query function based on user input and requests the required criteria for that query.

from queries import *

chosen_query = {
        "1": retrieve_flights_by_destination,
        "2": add_new_flight
    }

def handle_query(input_choice):
    #Catch invalid input??
    return chosen_query[input_choice]

def get_criteria(input_choice):
    if input_choice == "1":
        return input("Enter the destination ID to search for flights: ")
    elif input_choice == "2":
        pilot_id = input("Enter pilot ID: ")
        destination_id = input("Enter destination ID: ")
        aircraft_id = input("Enter aircraft ID: ")
        return (pilot_id, destination_id, aircraft_id)
