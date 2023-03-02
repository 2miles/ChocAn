from chocan import (
    input_system, 
    output_system, 
)

def display_provider_ui_menu() -> None:
    output_system.display(
        "\n\n"
        "************* PROVIDER MENU ************\n"
        "1. Check In Member\n"
        "2. Bill Member\n"
        "3. Provider Directory\n"
        "4. Exit\n"
        "----------------------------------------"
    )

def run_provider_ui() -> None:
    while True:
        display_provider_ui_menu()
        selection = input_system.get_input(1)
        match selection:
            case '1': output_system.display("TODO: check in member")
            case '2': output_system.display("TODO: bill member")
            case '3': output_system.display("TODO: generate provider directory")
            case '4': break
            case _:
                output_system.display(f'Unknown selection {selection}')