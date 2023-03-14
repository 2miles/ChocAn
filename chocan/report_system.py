from datetime import datetime
import service_system, member_system, provider_system, provider_directory_system, storage_system

def format_file_name(name : str) -> str:
    # replace whitespace with underscore
    s = "_".join(name.split())
    return s

# turns a list of records into a dictionary accessible by the record number
def group_by_number(records : list[any]) -> dict:
    result = {}
    for r in records:
        result[r.number] = r
    return result

# turns a list of services into a dictionary grouped by the member number so you
# can access all the services of a member by using the member number as a key
def group_by_member_number(records : list['service_system.ServiceRecord']) -> dict:
    result = {}
    for r in records:
        if r.member_number in result:
            result[r.member_number].append(r)
        else:
            result[r.member_number] = [r]
    return result

def _dated_file_name(name : str) -> str:
    formatted_name = format_file_name(name)
    date = datetime.today().strftime("%d-%m-%Y")
    file_name = f"{formatted_name}-{date}.txt"
    return file_name

def _member_service_info(service, providers) -> str:
    provider_name = providers[service.provider_number].name
    service_name = provider_directory_system.get_provider_service(service.service_code).name
    info = (
        f"Date of Service: {service.date_of_service}\n"
        f"Provider Name: {provider_name}\n"
        f"Service Name: {service_name}\n"
    )
    return info

def _build_member_service_report(member, services, providers) -> None:
    file_name = _dated_file_name(member.name)
    member_info = (
        f"Member Name: {member.name}\n"
        f"Member Number: {member.number}\n"
        f"Member Street: {member.street}\n"
        f"Member City: {member.city}\n"
        f"Member State: {member.state}\n"
        f"Member Zip: {member.zip}\n"
    )
    # TODO: sort `services` by date
    service_info = map(lambda s: _member_service_info(s, providers), services)
    service_info = "\n".join(service_info)
    info = (
        f"{member_info}\n"
        "Services:\n"
        f"{service_info}"
    )
    storage_system.create_report(file_name, info)

def _build_member_service_reports(members, services, providers) -> None:
    for n in list(services.keys()):
        _build_member_service_report(members[n], services[n], providers)

#TODO
def generate_provider_report() -> None:
    pass

def generate_member_service_report() -> None:
    members = group_by_number(member_system.get_all_members())
    providers = group_by_number(provider_system.get_all_providers())
    services = group_by_member_number(service_system.get_services_this_week())
    _build_member_service_reports(members, services, providers)
    pass

#TODO
def generate_mgmt_report() -> None:
    pass

#TODO
def generate_eft_report() -> None:
    pass
