import string
from chocan import (
    input_system, 
    output_system, 
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
  name = ask_for_name()
  street = ask_for_street()
  city = ask_for_city()
  state = ask_for_state()
  zip = ask_for_zip()
  member_system.create_member(name, street, city, state, zip)

def ask_for_name() -> string:
    while True:
        try:
            output_system.display("\nName: ")
            result = input_system.get_input(25)
        except ValueError:
            output_system.display("Invalid data. Try again.")
            continue
        break
    return result

def ask_for_street() -> string:
    while True:
        try:
            output_system.display("\nStreet Address: ")
            result = input_system.get_input(25)
        except ValueError:
            output_system.display("Invalid data. Try again.")
            continue
        break
    return result

def ask_for_city() -> string:
    while True:
        try:
            output_system.display("\nCity: ")
            result = input_system.get_input(14)
        except ValueError:
            output_system.display("Invalid data. Try again.")
            continue
        break
    return result

def ask_for_state() -> string:
    """
    Accepts first two letters of any string, then capitlizes it.
    """
    while True:
        try:
            output_system.display("\nState: ")
            result = input_system.get_input(2)
            result = result.upper()
        except ValueError:
            output_system.display("Invalid data. Try again.")
            continue
        break
    return result

def ask_for_zip() -> string:
    """
    Accepts any 5 digit integer
    """
    while True:
        try:
            output_system.display("\nZip code: ")
            result = int(input_system.get_input(5))
            if result > 99999 or result < 10000:
                raise ValueError
        except ValueError:
            output_system.display("Invalid data. Try again.")
            continue
        break
    return str(result)


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
  name = ask_for_name()
  street = ask_for_street()
  city = ask_for_city()
  state = ask_for_state()
  zip = ask_for_zip()
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
            case '1': output_system.display("TODO: update member record")
            case '2': output_system.display("TODO: delete member record")
            case '3': break
            case _:
                output_system.display(f"Unknown selection {selection}")


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
