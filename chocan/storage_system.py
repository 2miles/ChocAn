from enum import Enum
import json

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

def get_all_records(record_type : RecordType) -> "list[dict]":
    try:
        records = json.load(open(record_directory + _record_file_names[record_type]))
        return records
    except FileNotFoundError:
        return []
