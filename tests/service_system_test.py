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

def test_create_service_record(record_cleaner):
    service = service_system.create_service_record(
        provider_number = 12,
        member_number   = 20,
        member_name     = "Tim Apple",
        service_code    = 3,
        fee             = 500,
        date_of_service = "09-03-2023",
        date_received   = "09-03-2023 19:20:29",
    )
    assert service.provider_number  == 12
    assert service.member_number    == 20
    assert service.member_name      == "Tim Apple"
    assert service.service_code     == 3
    assert service.fee              == 500
    assert service.date_of_service  == "09-03-2023"
    assert service.date_received    == "09-03-2023 19:20:29"
