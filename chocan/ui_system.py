import string
from chocan import (
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
                provider_number = get_provider_number_ui()
                if(verify_provider_number(provider_number)):
                    provider_ui_system.run_provider_ui() 
            case '3': break
            case _:
                output_system.display(f"Unknown selection {selection}")

def get_provider_number_ui() -> int:
    """
    Promts user for provider number until they enter a positive integer. 
    Accepts integers larger than 9 digits but only considers the first 9 digits.
    Returns the potential provider number.
    """
    while True:
        try:
            output_system.display("\nEnter provider number")
            result = int(input_system.get_input(9))
            if result < 1:
                raise ValueError
        except ValueError:
            output_system.display("Invalid data. Try again.")
            continue
        break
    return result

# TODO i have this turned off for now, until we have some data in ./records/providers.json
def verify_provider_number(provider_number: int) -> bool:
    ## if provider_system.get_provider(provider_number) == None:
    ##     output_system.display("Provider does not exit")
    ##     return False
    return True
