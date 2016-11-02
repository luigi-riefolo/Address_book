#!/usr/bin/env python

"""

Design-only questions:

    Find person by email address

    User can supply any substring,
    ie. "comp" works assuming "alexander@company.com"
    is an email address in the address book.
    Discuss how you would implement this without coding the solution.
"""

from __future__ import print_function

import sys
import logging
from logging.config import fileConfig
from addressbook import AddressBook, Person

"""
Handler.createLock()
Initializes a thread lock which can be used to serialize access
to underlying I/O functionality which may not be threadsafe.

Handler.acquire()
Acquires the thread lock created with createLock().
"""

# logger.error("ERROR!!!!!!!!!!!!!")
# logger.error('Failed to open file', exc_info=True)


def main():
    """ Main """
    fileConfig(
        'logging.conf',
        defaults={'logfilename': 'addressbook.log'})
    logger = logging.getLogger(__name__)
    logger.info("Started")

    addr_book = AddressBook()
    person_args = {
        "lastname": "Mario",
        "name": "Luigi",
        "address": ["via alfa", "via beta"],
        "email": ["luigi.mario@gmail.com", "luigi@gmail.com"],
        "phone": ["012345678", "8765431"],
        "groups": ["Alfa", "Gamma"]
    }
    print("PERSON: %s" % person_args)
    person1 = Person(person_args)
    person_args = {
        "lastname": "Mario",
        "name": "Mario",
        "address": ["via alfa", "via beta"],
        "email": ["luigi.riefolo@gmail.com", "luigi@gmail.com"],
        "phone": ["012345678", "8765431"],
        "groups": ["Alfa", "Gamma"]
    }
    person2 = Person(person_args)
    # Add a group to the address book.
    addr_book.add_group("Alfa")
    addr_book.add_group("Gamma")
    addr_book.groups_to_str()

    # Add a group to the address book.

    # Add a person to the address book.
    addr_book.add_person(person1)
    addr_book.add_person(person2)
    print(addr_book.persons_to_str())
    print(addr_book.groups_to_str())

    # Given a group we want to easily find its members
    for person in addr_book.get_group_members("Alfa"):
        print("Person: %s" % person.get_full_name())

    # Given a person we want to easily find the groups the person belongs to.
    print("Person: " + str(addr_book.get_person_group(person1)))

    # Find person by name (can supply either first name, last name, or both).
    persons_found = addr_book.find_person("Riefolo", "Luigi")
    if persons_found is not None:
        for person in persons_found:
            print(person)
    print("--------------------------")
    persons_found = addr_book.find_person("Riefolo", None)
    if persons_found is not None:
        for person in persons_found:
            print(person)
    print("--------------------------")
    persons_found = addr_book.find_person(None, "Luigi")
    if persons_found is not None:
        for person in persons_found:
            print(person)

    print("--------------------------")
    # Find person by email address (can supply either the exact string
    # or a prefix string,
    # ie. both "alexander@company.com" and "alex" should work).
    person_found = addr_book.find_person_by_email("luigi.riefolo@gmail.com")
    if person_found is not None:
        print("Found: %s" % person_found)
        print("Found:\n%s" % person_found.get_fmt_str())


if __name__ == "__main__":
    sys.exit(main())
