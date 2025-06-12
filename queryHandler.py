# This file retrieves the correct query function based on user input and requests the required criteria for that query.

from queries import *

chosen_query = {
    "1": retrieve_flights_by_destination,
    "2": add_new_flight,
    "3": assign_pilot_to_flight,
    "4": view_pilot_schedule,
    "5": retrieve_departures_between_datetimes,
    }

# Dictionary mapping input choices to required input prompts
required_criteria = {
    "1": ["Enter the airport code to search for flights: "],
    "2": ["Enter pilot ID: ", "Enter destination ID: ", "Enter aircraft ID: "],
    "3": ["Enter pilot ID: ", "Enter flight ID: "],
    "4": ["Enter pilot ID to view schedule: "],
    "5": ["Enter start date and time (YYYY-MM-DD HH:MM:SS): ", "Enter end date and time (YYYY-MM-DD HH:MM:SS): "],

    }

def handle_query(input_choice):
    #Catch invalid input??
    return chosen_query[input_choice]

def get_criteria(input_choice):
    prompts = required_criteria[input_choice]
    responses = [input(prompt) for prompt in prompts]
    return responses

