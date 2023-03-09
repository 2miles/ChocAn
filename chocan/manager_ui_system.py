from chocan import (
    constants,
    input_system, 
    output_system, 
    ui_system,
    member_system,
    provider_system,
)

# Manager Menu
###############################################################################
def display_manager_ui_menu() -> None:
    output_system.display(
        "\n\n"
        "************* MANAGER MENU ************\n"
        "1. Manage Members\n"
        "2. Manage Providers\n"
        "3. Generate Reports\n"
        "4. Exit\n"
        "----------------------------------------"
    )

def run_manager_ui() -> None:
    while True:
        display_manager_ui_menu()
        selection = input_system.get_input(1)
        match selection:
            case '1': run_manage_members_ui()
            case '2': run_manage_providers_ui()
            case '3': run_generate_reports_ui()
            case '4': break
            case _:
                output_system.display(f"Unknown selection {selection}")


# Manage Members Menu
###############################################################################
def display_manage_members_ui_menu() -> None:
    output_system.display(
        "\n\n"
        "********** MANAGE MEMBERS MENU *********\n"
        "1. Create Member\n"
        "2. Lookup Member\n"
        "3. Back\n"
        "----------------------------------------"
    )

def run_manage_members_ui() -> None:
    while True:
        display_manage_members_ui_menu()
        selection = input_system.get_input(1)
        match selection:
            case '1': run_create_member_ui()
            case '2': run_lookup_member_ui()
            case '3': break
            case _:
                output_system.display(f"Unknown selection {selection}")

def run_create_member_ui() -> None:
    name = ui_system.ask_for_string("Name: ", constants.MAX_NAME)
    street = ui_system.ask_for_string("Street Address: ", constants.MAX_NAME)
    city = ui_system.ask_for_string("City: ", constants.MAX_CITY)
    state = ui_system.ask_for_string("State: ", constants.MAX_STATE).upper()
    zip = str(ui_system.ask_for_int("Zip: ", constants.MIN_ZIP, constants.MAX_ZIP))
    
    member_system.create_member(name, street, city, state, zip)


# Manage Providers Menu
###############################################################################
def display_manage_providers_ui_menu() -> None:
    output_system.display(
        "\n\n"
        "********* MANAGE PROVIDERS MENU ********\n"
        "1. Create Provider\n"
        "2. Lookup Provider\n"
        "3. Back\n"
        "----------------------------------------"
    )

def run_manage_providers_ui() -> None:
    while True:
        display_manage_providers_ui_menu()
        selection = input_system.get_input(1)
        match selection:
            case '1': run_create_provider_ui()
            case '2': run_lookup_provider_ui()
            case '3': break
            case _:
                output_system.display(f"Unknown selection {selection}")

def run_create_provider_ui() -> None:
    name = ui_system.ask_for_string("Name: ", constants.MAX_NAME)
    street = ui_system.ask_for_string("Street Address: ", constants.MAX_NAME)
    city = ui_system.ask_for_string("City: ", constants.MAX_CITY)
    state = ui_system.ask_for_string("State: ", constants.MAX_STATE).upper()
    zip = str(ui_system.ask_for_int("Zip: ", constants.MIN_ZIP, constants.MAX_ZIP))

    provider_system.create_provider(name, street, city, state, zip)


# Generate Reports Menu
###############################################################################
def display_generate_reports_ui_menu() -> None:
    output_system.display(
        "\n\n"
        "********* MANAGE PROVIDERS MENU ********\n"
        "1. Provider Report\n"
        "2. Member Service Report\n"
        "3. MGMT Report\n"
        "4. EFT Report\n"
        "5. Back\n"
        "----------------------------------------"
    )

def run_generate_reports_ui() -> None:
    while True:
        display_generate_reports_ui_menu()
        selection = input_system.get_input(1)
        match selection:
            case '1': output_system.display("TODO: generate provider report")
            case '2': output_system.display("TODO: generate member service report")
            case '3': output_system.display("TODO: generate MGMT report")
            case '4': output_system.display("TODO: generate EFT report")
            case '5': break
            case _:
                output_system.display(f"Unknown selection {selection}")


# Lookup Member Menu
###############################################################################
def display_lookup_manager_ui_menu() -> None:
    output_system.display(
        "\n\n"
        "********** LOOKUP MEMBER MENU **********\n"
        "1. Update Member\n"
        "2. Delete Member\n"
        "3. Back\n"
        "----------------------------------------"
    )

def run_lookup_member_ui() -> None:
    while True:
        display_lookup_manager_ui_menu()
        selection = input_system.get_input(1)
        match selection:
            case '1': run_update_member_ui()
            case '2': output_system.display("TODO: delete member record")
            case '3': break
            case _:
                output_system.display(f"Unknown selection {selection}")

def run_update_member_ui() -> None: 
    number = ui_system.ask_for_int("Enter member number: ", constants.MIN_USER_NUM, constants.MAX_USER_NUM)
    if member_system.get_member(number) == None:
        output_system.display("That member does not exitst")
        return
    name = ui_system.ask_for_string("Name: ", constants.MAX_NAME)
    street = ui_system.ask_for_string("Street Address: ", constants.MAX_NAME)
    city = ui_system.ask_for_string("City: ", constants.MAX_CITY)
    state = ui_system.ask_for_string("State: ", constants.MAX_STATE).upper()
    zip = str(ui_system.ask_for_int("Zip: ", constants.MIN_ZIP, constants.MAX_ZIP))
    activity = ui_system.ask_yes_or_no("Active: (y/n)")
    deleted = ui_system.ask_yes_or_no("Deleted: (y/n)")

    member_system.update_member(name, street, city, state, zip, activity, number, deleted)


# Lookup Provider Menu
###############################################################################
def display_lookup_provider_ui_menu() -> None:
    output_system.display(
        "\n\n"
        "********* LOOKUP PROVIDER MENU *********\n"
        "1. Update Provider\n"
        "2. Delete Provider\n"
        "3. Back\n"
        "----------------------------------------"
    )

def run_lookup_provider_ui() -> None:
    while True:
        display_lookup_provider_ui_menu()
        selection = input_system.get_input(1)
        match selection:
            case '1': output_system.display("TODO: update provider record")
            case '2': output_system.display("TODO: delete provider record")
            case '3': break
            case _:
                output_system.display(f"Unknown selection {selection}")