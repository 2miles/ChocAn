from chocan import service_system

def test_get_all_services(storage_records):
    services = service_system.get_all_services()
    assert len(services) == 1
    assert services[0].provider_number == 1
    assert services[0].member_number == 1
    assert services[0].member_name == "Patty Tester"
    assert services[0].service_code == 1
    assert services[0].fee == 4550
    assert services[0].date_of_service == "2023-10-05T14:48:00.000Z"
    assert services[0].date_received == "2023-10-05T14:48:00.000Z"

# TODO:
# create_service