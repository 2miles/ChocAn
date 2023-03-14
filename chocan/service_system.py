from datetime import datetime, timedelta
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

    def date_of_service_pretty(self) -> str:
        d = datetime.fromisoformat(self.date_of_service).strftime("%d-%m-%Y")
        return d

    def date_received_pretty(self) -> str:
        d = datetime.fromisoformat(self.date_received).strftime("%d-%m-%Y %H:%M:%S")
        return d

# mon = 1, sun = 7
# how many days ago was saturday?
_days_ago = { 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 0, 7: 1 }

def _is_this_week(record) -> bool:
    now = datetime.now()
    # Saturday @ 00:00:00 AM
    sat = (now - timedelta(days = _days_ago[now.isoweekday()])).replace(hour=0, minute=0, second=0)
    record_date = datetime.fromisoformat(record['date_of_service'])
    return (sat < record_date)

def get_all_services() -> list['ServiceRecord']:
    records = storage_system.get_all_records(storage_system.RecordType.SERVICE)
    records = list(map(lambda r : ServiceRecord(r), records))
    return records

def create_service_record(
    provider_number : int,
    member_number   : int,
    member_name     : str,
    service_code    : int,
    fee             : int,
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

def _sort_service(record):
    return datetime.fromisoformat(record.date_of_service)

def get_services_this_week() -> list['ServiceRecord']:
    records = storage_system.get_all_records(storage_system.RecordType.SERVICE)
    records = list(map(lambda r: ServiceRecord(r), list(filter(_is_this_week, records))))
    records.sort(key=_sort_service)
    return records