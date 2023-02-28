from enum import Enum
import json

class RecordType(Enum):
    MEMBER   = 1
    PROVIDER = 2
    SERVICE  = 3

record_file_names = {
  RecordType.MEMBER   : "members.txt",
  RecordType.PROVIDER : "providers.txt",
  RecordType.SERVICE  : "services.txt"
}

record_directory = "./records/"

def get_all_records(record_type : RecordType) -> "list[dict]":
    try:
        records = json.load(open(record_directory + record_file_names[record_type]))
        return records
    except FileNotFoundError:
        return []
