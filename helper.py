
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported conversion unit"


def validate_and_execute(days_and_unit_dict):
    try:
        my_int_input = int(days_and_unit_dict["days"])
        if my_int_input > 0:
            my_result = days_to_units(my_int_input, days_and_unit_dict["unit"])
            print(my_result)
        elif my_int_input == 0:
            print("You entered a 0, please enter a valid positive number!")
        else:
            print("You entered a negative number, please enter a valid positive number!")
    except ValueError:
        print("your input is not a number. Don't ruin my program!")


user_input_message = "please enter a number and conversion unit\n"
