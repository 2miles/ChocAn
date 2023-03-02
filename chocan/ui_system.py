from chocan import (
    input_system, 
    output_system, 
    manager_ui_system, 
    provider_ui_system,
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
                if(verify_manager()):
                    manager_ui_system.run_manager_ui() 
            case '2': 
                if(verify_provider()):
                    provider_ui_system.run_provider_ui() 
            case '3': break
            case _:
                output_system.display(f"Unknown selection {selection}")


# TODO: this needs to be implemented
def verify_manager() -> bool:
    return True

# TODO: this needs to be implemented
def verify_provider() -> bool:
    return True