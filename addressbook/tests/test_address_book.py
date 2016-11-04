"""
    addressbook unit tests
"""

from __future__ import print_function

import unittest
from addressbook import AddressBook, Person


class TestAddressbook(unittest.TestCase):
    """
        Address book unit test class.
    """
    group1 = "Alfa"
    group2 = "Gamma"

    person_args = {
        "lastname": "Mario",
        "name": "Luigi",
        "address": ["via alfa", "via beta"],
        "email": ["luigi.mario@gmail.com", "luigi@gmail.com"],
        "phone": ["012345678", "8765431"],
        "groups": ["Alfa", "Gamma"]
    }
    person1 = Person(person_args)

    person_args = {
        "lastname": "Mario",
        "name": "Luigi",
        "address": ["via alfa", "via beta"],
        "email": ["luigi.mario@gmail.com", "luigi@gmail.com"],
        "phone": ["012345678", "8765431"],
        "groups": ["Alfa", "Gamma"]
    }
    person2 = Person(person_args)

    def test_add_person(self):
        """ Add a group to the address book. """
        addr_book = AddressBook()
        addr_book.add_person(self.person1)
        k = self.person1.get_lastname() + "_" + self.person1.get_name()
        self.assertTrue(k in addr_book.persons)

    def test_person_not_in_address_book(self):
        """ Check that a person does not exist. """
        addr_book = AddressBook()
        k = "Mario_Luigi"
        self.assertFalse(k in addr_book.persons)

    def test_add_group(self):
        """ Add a group to the address book. """
        addr_book = AddressBook()
        addr_book.add_group(self.group1)
        self.assertTrue(self.group1 in addr_book.groups)

    def test_find_group_members(self):
        """ Given a group we want to easily find its members. """
        addr_book = AddressBook()
        addr_book.add_group(self.group2)
        addr_book.add_person(self.person1)
        addr_book.add_person(self.person2)
        for person in addr_book.get_group_members(self.group2):
            print("Person: " + person.get_full_name())
            self.assertTrue(isinstance(person.get_full_name(), basestring))

    def test_get_person_groups(self):
        """ Find person's groups. """
        addr_book = AddressBook()
        addr_book.add_group(self.group2)
        addr_book.add_person(self.person1)
        groups = addr_book.get_person_group(self.person1)
        self.assertIsNotNone(groups)
        print("Groups: " + str(groups))

    def test_find_person_by_fullname(self):
        """
        Find person by name.

        Supplying either first name, last name, or both.
        """
        addr_book = AddressBook()
        addr_book.add_person(self.person1)
        persons = addr_book.find_person("Mario", "Luigi")
        self.assertIsNotNone(persons)
        print("P:::::::: " + str(persons))
        for person in persons:
            print(person.get_fmt_str())

    def test_find_person_by_lastname(self):
        """ Find person by lastname. """
        addr_book = AddressBook()
        addr_book.add_person(self.person1)
        persons = addr_book.find_person("Mario", None)
        self.assertIsNotNone(persons)
        for person in persons:
            print(person.get_fmt_str())

    def test_find_person_by_name(self):
        """ Find person by name. """
        addr_book = AddressBook()
        addr_book.add_person(self.person1)
        persons = addr_book.find_person(None, "Luigi")
        self.assertIsNotNone(persons)
        for person in persons:
            print(person.get_fmt_str())

    def test_find_person_by_email(self):
        """
        Find person by email address.

        Supplying either the exact string or a prefix string,
        ie. both "alexander@company.com" and "alex" work).
        """
        addr_book = AddressBook()
        addr_book.add_person(self.person1)
        person = addr_book.find_person_by_email("luigi.mario@gmail.com")
        self.assertIsNotNone(person)
        print("Person found")

    def test_find_person_partial_email(self):
        """ Find person by partial email. """
        addr_book = AddressBook()
        addr_book.add_person(self.person1)
        person = addr_book.find_person_by_email("uigi")
        self.assertIsNotNone(person)
        print("Person found")


if __name__ == '__main__':
    unittest.main()
