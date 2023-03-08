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