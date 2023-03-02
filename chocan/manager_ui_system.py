from chocan import (
    input_system, 
    output_system, 
)

# MANAGE MANAGER MENU
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


# MANAGE MEMBERS MENU
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
            case '1': output_system.display("TODO: create member")
            case '2': run_lookup_member_ui()
            case '3': break
            case _:
                output_system.display(f"Unknown selection {selection}")


# MANAGE PROVIDERS MENU
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
            case '1': output_system.display("TODO: create provider")
            case '2': run_lookup_provider_ui()
            case '3': break
            case _:
                output_system.display(f"Unknown selection {selection}")


# GENERATE REPORTS MENU
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


# LOOKUP MEMBER MENU
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


# LOOKUP PROVIDER MENU
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
