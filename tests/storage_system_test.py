from chocan import storage_system, provider_system, member_system
import pytest
import os

# Loading `storage_records` fixture changes `storage_system.record_directory` to point
# towards the "records" folder in the "test" directory.
@pytest.fixture
def storage_records():
    old_path = storage_system.record_directory
    fixture_record_folder = os.path.dirname(os.path.abspath(__file__)) + "/records/"
    storage_system.record_directory = fixture_record_folder
    yield fixture_record_folder
    storage_system.record_directory = old_path

def _get_json_cache(file_path : str) -> str:
    file = open(file_path, "r")
    json = file.read()
    file.close()
    return json

def _write_json_cache(json : str, file_path : str) -> None:
    file = open(file_path, "w")
    file.write(json)
    file.close()
    return None

# Loading the `record_cleaner` fixture will store a cache of the current json records
# in the "records" folder in the "test" directory. When the fixture ends, it will restore
# the json records to the state in the cache. This allows tests to modify records without
# making persistent changes to the files after the tests are done.
@pytest.fixture
def record_cleaner(storage_records):
    member_path   = storage_system.file_path(storage_system.RecordType.MEMBER)
    provider_path = storage_system.file_path(storage_system.RecordType.PROVIDER)
    service_path  = storage_system.file_path(storage_system.RecordType.SERVICE)
    member_json   = _get_json_cache(member_path)
    provider_json = _get_json_cache(provider_path)
    service_json  = _get_json_cache(service_path)
    yield
    _write_json_cache(member_json, member_path)
    _write_json_cache(provider_json, provider_path)
    _write_json_cache(service_json, service_path)

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

def test_get_all_providers(record_cleaner):
    providers = provider_system.get_all_providers()
    assert len(providers) == 2
    assert providers[0].name   == "Provider 1"
    assert providers[0].street == "Office Street"
    assert providers[0].city   == "Portland"
    assert providers[0].state  == "OR"
    assert providers[0].zip    == "97214"
    assert providers[0].number == 1

    assert providers[1].name   == "Provider 2"
    assert providers[1].street == "Provider Ave"
    assert providers[1].city   == "Portland"
    assert providers[1].state  == "OR"
    assert providers[1].zip    == "97222"
    assert providers[1].number == 2

def test_create_provider(record_cleaner):
    provider = provider_system.create_provider(
        name   = "Provider 3",
        street = "3rd Ave",
        city   = "Portland",
        state  = "OR",
        zip    = "34567"
    )
    assert provider.name   == "Provider 3"
    assert provider.street == "3rd Ave"
    assert provider.city   == "Portland"
    assert provider.state  == "OR"
    assert provider.zip    == "34567"
    assert provider.number == 3

    # Check that the provider was actually created in the storage system.
    all_providers = provider_system.get_all_providers()
    assert len(all_providers)      == 3
    assert all_providers[2].name   == "Provider 3"
    assert all_providers[2].number == 3

def test_get_provider(record_cleaner):
    # fetches an existing provider record 
    provider = provider_system.get_provider(1)
    assert provider.number == 1

    # fetches a non-existing provider record 
    provider = provider_system.get_provider(999999999)
    assert provider is None

def test_update_provider(record_cleaner):
    provider = provider_system.update_provider(
        name   = "Updated Provider 1",
        street = "Updated Street",
        city   = "Portland",
        state  = "OR",
        zip    = "97214",
        number = 1
    )
    assert provider.name   == "Updated Provider 1"
    assert provider.street == "Updated Street"
    assert provider.city   == "Portland"
    assert provider.state  == "OR"
    assert provider.zip    == "97214"
    assert provider.number == 1

    # Check that the provider was updated in the storage system.
    updated_provider = provider_system.get_provider(1)
    assert updated_provider.name   == "Updated Provider 1"
    assert updated_provider.street == "Updated Street"

def test_delete_provider(record_cleaner):
    provider_system.delete_provider(2)

    # Check that provider 2 was deleted from the storage system.
    del_provider = provider_system.get_provider(2)
    del_provider == None

def test_create_member(record_cleaner):
    member = member_system.create_member(
        name   = "Member 4",
        street = "3rd Ave",
        city   = "Portland",
        state  = "OR",
        zip    = "34567"
    )
    assert member.name   == "Member 4"
    assert member.street == "3rd Ave"
    assert member.city   == "Portland"
    assert member.state  == "OR"
    assert member.zip    == "34567"
    assert member.number == 4

def test_get_all_members(record_cleaner):
    members = member_system.get_all_members()
    assert len(members) == 3
    assert members[0].name   == "Patty Tester"
    assert members[0].street == "123 Alphabet"
    assert members[0].city   == "Portlandia"
    assert members[0].state  == "OR"
    assert members[0].zip    == "97214"
    assert members[0].number == 1

    assert members[1].name   == "Steven Software"
    assert members[1].street == "10th Circle"
    assert members[1].city   == "Vancouver"
    assert members[1].state  == "WA"
    assert members[1].zip    == "98686"
    assert members[1].number == 2

    assert members[2].name   == "Taylor Todds"
    assert members[2].street == "1900 Morrison St"
    assert members[2].city   == "Portlandia"
    assert members[2].state  == "OR"
    assert members[2].zip    == "97214"
    assert members[2].number == 3