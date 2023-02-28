from chocan import storage_system

def test_get_all_records_empty():
    records = storage_system.get_all_records(storage_system.RecordType.MEMBER)
    assert (len(records) == 0)