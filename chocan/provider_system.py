from chocan import storage_system

class InvalidProviderNumber(Exception):
    pass

class ProviderRecord:
    def __init__(self, data: dict):
        self.name    = data["name"]
        self.street  = data["street"]
        self.city    = data["city"]
        self.state   = data["state"]
        self.zip     = data["zip"]
        self.number  = data["number"]
        self.deleted = data["deleted"]

def generate_provider_number() -> int:
    members = storage_system.get_all_records(storage_system.RecordType.PROVIDER)
    number = max(map(lambda r : r["number"], members)) + 1 if members else 1
    if number > 999999999:
        raise InvalidProviderNumber("Provider number too large: " + str(number))
    return number

def create_provider(
    name    : str,
    street  : str,
    city    : str,
    state   : str,
    zip     : str
) -> 'ProviderRecord':
    number = generate_provider_number()

    data = {
        "name"   : name,
        "street" : street,
        "city"   : city,
        "state"  : state,
        "zip"    : zip,
        "number" : number,
        "deleted" : False
    }

    provider_record = ProviderRecord(data)
    storage_system.create_record(storage_system.RecordType.PROVIDER, data)
    return provider_record

def update_provider(
    name    : str,
    street  : str,
    city    : str,
    state   : str,
    zip     : str,
    number  : int,
    deleted : bool
) -> 'ProviderRecord':
    data = {
        "name"   : name,
        "street" : street,
        "city"   : city,
        "state"  : state,
        "zip"    : zip,
        "number" : number,
        "deleted" : deleted
    }
    provider_record = ProviderRecord(data)
    storage_system.update_record(storage_system.RecordType.PROVIDER, number, data)
    return provider_record

def get_all_providers() -> list['ProviderRecord']:
    records = storage_system.get_all_records(storage_system.RecordType.PROVIDER)
    records = list(map(lambda r : ProviderRecord(r), records))
    return records

def get_provider(number: int) -> 'ProviderRecord' | None:
    record = storage_system.get_record(storage_system.RecordType.PROVIDER, number)
    return ProviderRecord(record) if record else None

def delete_provider(number: int) -> None:
    storage_system.delete_record(storage_system.RecordType.PROVIDER, number)
    return None
