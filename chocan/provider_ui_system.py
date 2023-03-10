from datetime import datetime
from chocan import (
    input_system, 
    output_system, 
    member_system,
    service_system,
    constants,
    ui_util
)


def get_service_record_input() -> dict:
    provider_number = str(ui_util.ask_for_int("Provider #: ", constants.MIN_USER_NUM, constants.MAX_USER_NUM))
    member_number   = str(ui_util.ask_for_int("Member #: ", constants.MIN_USER_NUM, constants.MAX_USER_NUM))
    member_name     = ui_util.ask_for_string("Member name: ", constants.MAX_NAME)
    service_code    = str(ui_util.ask_for_int("Service code: ", constants.MIN_CODE, constants.MAX_CODE))
    fee             = str(ui_util.ask_for_int("Service fee: ", constants.MIN_FEE, constants.MAX_FEE))
    today           = datetime.today()
    now             = datetime.now()
    date_of_service = today.strftime("%d-%m-%Y")
    date_received   = now.strftime("%d-%m-%Y %H:%M:%S")
    comments        = ui_util.ask_for_string("Comments: ", constants.MAX_COMMENT)

    record  = {
        'provider_number': provider_number,
        'member_number': member_number,
        'member_name': member_name,
        'service_code': service_code,
        'fee': fee,
        'date_of_service' : date_of_service,
        'date_received' : date_received,
        'comments' : comments
    }
    return record

# Provider Menu
###############################################################################
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
            case '1': run_checkin_member_ui() 
            case '2': run_bill_member_ui()
            case '3': output_system.display("TODO: generate provider directory")
            case '4': break
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

def run_bill_member_ui() -> None:
    number = ui_util.ask_for_int("Enter member number: ", constants.MIN_USER_NUM, constants.MAX_USER_NUM)
    member = member_system.get_member(number)
    output_system.display("Validated")
    run_create_service_record_ui()

def run_create_service_record_ui() -> None:
    record = get_service_record_input()
    service_record = service_system.create_service_record(
        record['provider_number'],
        record['member_number'],
        record['member_name'],
        record['service_code'],
        record['fee'],
        record['date_of_service'],
        record['date_received'],
        record['comments']
    )
    output_system.display("\nService Record Created\n")