from chocan import storage_system

class ServiceRecord:
    def __init__(self, data: dict):
        self.provider_number = data['provider_number']
        self.member_number = data['member_number']
        self.member_name = data['member_name']
        self.service_code = data['service_code']
        self.fee = data['fee']
        self.date_of_service = data['date_of_service']
        self.date_received = data['date_received']

def get_all_services() -> list['ServiceRecord']:
    records = storage_system.get_all_records(storage_system.RecordType.SERVICE)
    records = list(map(lambda r : ServiceRecord(r), records))
    return records

def create_service_record(
    provider_number : int,
    member_number   : int,
    member_name     : str,
    service_code    : int,
    fee             : float,
    date_of_service : str,
    date_received   : str,
) -> 'ServiceRecord':
    # Create a dictionary for "data" using dictionary comprehension
    data = {
        "provider_number" : provider_number,
        "member_number"   : member_number,
        "member_name"     : member_name,
        "service_code"    : service_code,
        "fee"             : fee,
        "date_of_service" : date_of_service,
        "date_received"   : date_received,
    }
    service_record = ServiceRecord(data)
    storage_system.create_record(storage_system.RecordType.SERVICE, data)
    return service_record