# This file retrieves the correct query function based on user input and requests the required criteria for that query.

from queries import *

# This dictionary maps user input choices to the corresponding query functions
chosen_query = {
    "1": retrieve_flights_by_criteria,  
    "2": add_new_flight,
    "3": assign_pilot_to_flight,
    "4": view_pilot_schedule,
    "5": retrieve_departures_between_datetimes,
    "6": retrieve_arrivals_between_datetimes,
    "7": update_flight_schedule,
    "8": delete_flight,
    "9": view_all_flights,
    }


# Dictionary mapping input choices to required input prompts
required_criteria = {
    "1": ["Select search field: ('destination', 'origin', 'airline', 'departure_date'): ", "Enter the value to search for:\n(Use airport codes, date format must be YYYY-MM-DD)"],
    "2": ["Enter pilot ID: ", "Enter destination ID: ", "Enter aircraft ID: "],
    "3": ["Enter pilot ID: ", "Enter flight ID: "],
    "4": ["Enter pilot ID to view schedule: "],
    "5": ["Enter start date and time (YYYY-MM-DD HH:MM:SS): ", "Enter end date and time (YYYY-MM-DD HH:MM:SS): "],
    "6": ['Enter start date and time (YYYY-MM-DD HH:MM:SS): ', 'Enter end date and time (YYYY-MM-DD HH:MM:SS): '],
    "7": ["Enter flight ID to update: ", "Enter new departure date and time (YYYY-MM-DD HH:MM:SS): ", "Enter new arrival date and time (YYYY-MM-DD HH:MM:SS): ", "Enter new flight status ('ON TIME', 'DELAYED' or 'DEPARTED'): "],
    "8": ["Enter flight ID to delete: "],
    "9": [],  # No criteria needed for viewing all flights
    }

def handle_query(input_choice):
    # Input handling for the query selection, if chosen query is not in the dictionary, it will prompt the user to try again.
    try:
        return chosen_query[input_choice]
    except KeyError:
        print("Invalid choice. Please try again.")
        return None

# This function retrieves the criteria required for the selected query from the user, in the form of a list of responses.
def get_criteria(input_choice):
    prompts = required_criteria[input_choice]
    responses = [input(prompt) for prompt in prompts]
    return responses

