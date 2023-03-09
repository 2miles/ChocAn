from chocan import (
    input_system, 
    output_system, 
    member_system,
    constants,
    ui_util
)

def display_provider_ui_menu() -> None:
    output_system.display(
        "\n\n"
        "************* PROVIDER MENU ************\n"
        "1. Check In Member\n"
        "2. Provider Directory\n"
        "3. Exit\n"
        "----------------------------------------"
    )

def run_provider_ui() -> None:
    while True:
        display_provider_ui_menu()
        selection = input_system.get_input(1)
        match selection:
            case '1': run_checkin_member_ui() 
            case '2': output_system.display("TODO: generate provider directory")
            case '3': break
            case _:
                output_system.display(f'Unknown selection {selection}')


def run_checkin_member_ui() -> None:
    number = ui_util.ask_for_int("Enter member number: ", constants.MIN_USER_NUM, constants.MAX_USER_NUM)
    member = member_system.get_member(number)
    if member == None:
        output_system.display("That member does not exist")
    elif member.active == False:
        output_system.display("Member Suspended")
    else:
        output_system.display("Validated")
        run_bill_member_ui()
    
def run_bill_member_ui() -> None:
    output_system.display("Service completed, time for billing")
    number = ui_util.ask_for_int("Enter member number: ", constants.MIN_USER_NUM, constants.MAX_USER_NUM)
    member = member_system.get_member(number)
    output_system.display("Validated")
    output_system.display("TODO: create service record")