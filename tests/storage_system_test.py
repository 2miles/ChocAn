from chocan import storage_system

def test_get_all_records_empty():
    records = storage_system.get_all_records(storage_system.RecordType.MEMBER)
    assert (len(records) == 0)
    records = storage_system.get_all_records(storage_system.RecordType.PROVIDER)
    assert (len(records) == 0)
    records = storage_system.get_all_records(storage_system.RecordType.SERVICE)
    assert (len(records) == 0)

def test_get_all_records_many(storage_records):
    records = storage_system.get_all_records(storage_system.RecordType.MEMBER)
    assert (len(records) == 3)
    records = storage_system.get_all_records(storage_system.RecordType.PROVIDER)
    assert (len(records) == 2)
    records = storage_system.get_all_records(storage_system.RecordType.SERVICE)
    assert (len(records) == 1)

def test_create_record_member(record_cleaner):
    records = storage_system.get_all_records(storage_system.RecordType.MEMBER)
    # Test that there is no record with member number 4242.
    assert not next((x for x in records if x['number'] == 4242), None)
    record = {
        "name": "Test Member",
        "street": "Street Ave",
        "city": "Portland",
        "state": "OR",
        "zip": "97214",
        "number": 4242
    }
    storage_system.create_record(storage_system.RecordType.MEMBER, record)
    records = storage_system.get_all_records(storage_system.RecordType.MEMBER)
    # Test that the record with member number 4242 exists.
    assert next((x for x in records if x['number'] == 4242), None)

# TODO:
# get_record
# update_record
# delete_record
# create_report