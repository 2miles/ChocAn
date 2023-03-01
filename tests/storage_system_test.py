from chocan import storage_system
import pytest
import os

# NOTE: loading `storage_records` fixture changes `storage_system.record_directory`
# Reference: https://docs.pytest.org/en/6.2.x/fixture.html#yield-fixtures-recommended
@pytest.fixture
def storage_records():
    old_path = storage_system.record_directory
    fixture_record_folder = os.path.dirname(os.path.abspath(__file__)) + "/records/"
    storage_system.record_directory = fixture_record_folder
    yield fixture_record_folder
    storage_system.record_directory = old_path

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