import string
from chocan import (
    constants,
    input_system, 
    output_system, 
    manager_ui_system, 
    provider_ui_system,
    provider_system,
)

def display_main_ui_menu() -> None:
    output_system.display(
        "\n\n"
        "*************** MAIN MENU **************\n"
        "1. Manager Login\n"
        "2. Provider Login\n"
        "3. Shutdown system\n"
        "----------------------------------------"
    )

def run_ui() -> None:
    while True:
        display_main_ui_menu()
        selection = input_system.get_input(1)
        match selection:
            case '1': 
                manager_ui_system.run_manager_ui() 
            case '2': 
                number = ask_for_int("Enter provider number: ", constants.MIN_USER_NUM, constants.MAX_USER_NUM)
                if(verify_provider_number(number)):
                    provider_ui_system.run_provider_ui() 
            case '3': break
            case _:
                output_system.display(f"Unknown selection {selection}")


# TODO i have this turned off for now, until we have some data in ./records/providers.json
def verify_provider_number(provider_number: int) -> bool:
    ## if provider_system.get_provider(provider_number) == None:
    ##     output_system.display("Provider does not exit")
    ##     return False
    return True


def ask_for_string(prompt: string, length: int) -> string:
    while True:
        try:
            output_system.display("\n" + prompt)
            result = input_system.get_input(length)
        except ValueError:
            output_system.display("Invalid data. Try again.")
            continue
        break
    return result

def ask_for_int(prompt: string, min: int, max: int) -> int:
    while True:
        try:
            output_system.display("\n" + prompt)
            result = int(input_system.get_input(25))
            if result > max or result < min:
                raise ValueError
        except ValueError:
            output_system.display("Invalid data. Try again.")
            continue
        break
    return result

def ask_yes_or_no(prompt: string) -> bool:
    while True:
        try:
            output_system.display("\n" + prompt)
            result = input_system.get_input(2)
            result = result.lower()
            if result != "y" or result != "n":
                raise ValueError
            if result == "n":
                return False
        except ValueError:
            output_system.display("Invalid data. Try again.")
            continue
        break
    return True