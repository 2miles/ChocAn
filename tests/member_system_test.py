from chocan import member_system
import os

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