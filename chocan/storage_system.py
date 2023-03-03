from enum import Enum
import json

class InvalidRecordType(Exception):
    pass

class RecordType(Enum):
    MEMBER   = 1
    PROVIDER = 2
    SERVICE  = 3

_record_file_names = {
  RecordType.MEMBER   : "members.json",
  RecordType.PROVIDER : "providers.json",
  RecordType.SERVICE  : "services.json"
}

record_directory = "./records/"

# A simple helper for getting the full file path to the record of the
# given record type.
def file_path(record_type : RecordType) -> str:
    return record_directory + _record_file_names[record_type]

def get_all_records(record_type : RecordType) -> "list[dict]":
    try:
        records = json.load(open(file_path(record_type), "r"))
        return records
    except FileNotFoundError:
        return []

def create_record(record_type : RecordType, data : dict) -> None:
    records = get_all_records(record_type)
    records.append(data)
    json.dump(records, open(file_path(record_type), "w"))
    return None

def get_index_of_record(records: list, number: int) -> int:
    for i in range(len(records)):
        if records[i]["number"] == number:
            return i
    return None

def get_record(record_type: RecordType, number: int) -> "list[dict]":
    if record_type == RecordType.SERVICE:
        raise InvalidRecordType("Service records not supported.")
    records = get_all_records(record_type)
    record_index = get_index_of_record(records, number)
    if record_index is not None:
        return records[record_index]
    else:
        return None
