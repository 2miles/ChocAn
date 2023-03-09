from chocan import (
    constants,
    input_system,
    output_system,
    ui_util,
    member_system,
    provider_system,
    ui_util
)

def get_record_input() -> dict:
    name    = ui_util.ask_for_string("Name: ", constants.MAX_NAME)
    street  = ui_util.ask_for_string("Street Address: ", constants.MAX_NAME)
    city    = ui_util.ask_for_string("City: ", constants.MAX_CITY)
    state   = ui_util.ask_for_string("State: ", constants.MAX_STATE).upper()
    zip     = str(ui_util.ask_for_int("Zip: ", constants.MIN_ZIP, constants.MAX_ZIP))
    record  = {
        'name': name,
        'street': street,
        'city': city,
        'state': state,
        'zip': zip
    }
    return record

def display_member(member : 'member_system.MemberRecord') -> None:
    output_system.display(
        f"Name: {member.name}\n"
        f"Street: {member.street}\n"
        f"City: {member.city}\n"
        f"State: {member.state}\n"
        f"Zip: {member.zip}\n"
        f"Active: {member.active}\n"
        f"Number: {member.number}\n"
    )

def display_provider(provider : 'provider_system.ProviderRecord') -> None:
    output_system.display(
        f"Name: {provider.name}\n"
        f"Street: {provider.street}\n"
        f"City: {provider.city}\n"
        f"State: {provider.state}\n"
        f"Zip: {provider.zip}\n"
        f"Number: {provider.number}\n"
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
        "3. Update Member\n"
        "4. Back\n"
        "----------------------------------------"
    )

def run_manage_members_ui() -> None:
    while True:
        display_manage_members_ui_menu()
        selection = input_system.get_input(1)
        match selection:
            case '1': run_create_member_ui()
            case '2': run_lookup_member_ui()
            case '2': run_update_member_ui()
            case '4': break
            case _:
                output_system.display(f"Unknown selection {selection}")

def run_create_member_ui() -> None:
    record = get_record_input()
    member = member_system.create_member(
        record['name'],
        record['street'],
        record['city'],
        record['state'],
        record['zip']
    )
    output_system.display("Member Created!\n")
    display_member(member)

def run_lookup_member_ui() -> None:
    number = ui_util.ask_for_int("Enter member number: ", constants.MIN_USER_NUM, constants.MAX_USER_NUM)
    member = member_system.get_member(number)
    if member == None:
        output_system.display("That member does not exist")
        return
    display_member(member)


def run_update_member_ui() -> None:
    number = ui_util.ask_for_int("Enter member number: ", constants.MIN_USER_NUM, constants.MAX_USER_NUM)
    member = member_system.get_member(number)
    if member == None:
        output_system.display("That member does not exist")
        return
    record = get_record_input()
    member_system.update_member(
        record['name'],
        record['street'],
        record['city'],
        record['state'],
        record['zip'],
        member.active,
        number,
        member.deleted
    )
    output_system.display("Member Updated!\n")

# Manage Providers Menu
###############################################################################
def display_manage_providers_ui_menu() -> None:
    output_system.display(
        "\n\n"
        "********* MANAGE PROVIDERS MENU ********\n"
        "1. Create Provider\n"
        "2. Lookup Provider\n"
        "3. Update Provider\n"
        "4. Back\n"
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
            case '4': break
            case _:
                output_system.display(f"Unknown selection {selection}")

def run_create_provider_ui() -> None:
    record = get_record_input()
    provider = provider_system.create_provider(
        record['name'],
        record['street'],
        record['city'],
        record['state'],
        record['zip']
    )
    output_system.display("Provider Created!\n")
    display_provider(provider)

def run_lookup_provider_ui() -> None:
    number = ui_util.ask_for_int("Enter provider number: ", constants.MIN_USER_NUM, constants.MAX_USER_NUM)
    provider = provider_system.get_provider(number)
    if provider == None:
        output_system.display("That provider does not exist")
        return
    display_provider(provider)

def run_update_provider_ui() -> None:
    number = ui_util.ask_for_int("Enter provider number: ", constants.MIN_USER_NUM, constants.MAX_USER_NUM)
    provider = provider_system.get_provider(number)
    if provider == None:
        output_system.display("That provider does not exist")
        return
    record = get_record_input()
    provider_system.update_provider(
        record['name'],
        record['street'],
        record['city'],
        record['state'],
        record['zip'],
        number,
        provider.deleted
    )
    output_system.display("Provider Updated!\n")

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
