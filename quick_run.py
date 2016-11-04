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
import logging.handlers
from addressbook import AddressBook, Person
import coloredlogs

# logger.error("ERROR!!!!!!!!!!!!!")
# logger.error('Failed to open file', exc_info=True)
LOG_FILENAME = "addressbook.log"
ERROR_FILENAME = "errors.log"


def main():
    """ Main """
    # fileConfig(
    #    'logging.conf',
    #    defaults={'logfilename': ''})

    log_format = (
        "[%(asctime)s] [%(levelname)s] "
        "[%(name)s] [%(funcName)s():%(lineno)s] "
        "[PID:%(process)d TID:%(thread)d] %(message)s")

#    logging.basicConfig(
#        level=logging.INFO,
#        format=log_format,
#        datefmt="%d/%m/%Y %H:%M:%S",
#        filename=LOG_FILENAME,
#        filemode='a')
#
#    logger = logging.getLogger(__name__)
#    handler = logging.handlers.RotatingFileHandler(
#        LOG_FILENAME,
#        maxBytes=200,
#        backupCount=5)
#

    # TODO:
    # IN COLORED LOGS:
    # ADD OPTION FOR ERRSTREAM/FILE
    # ADD OPTION FOR LOGROTATE
    # CHANGE LEVEL NAME COLOUR ACCORDING TO CURRENT LEVEL
    coloredlogs.install(
        level=logging.INFO,
        fmt=log_format,
        isatty=True,
        datefmt="%d/%m/%Y %H:%M:%S",
        stream=open(LOG_FILENAME, "w+"))

#    error_handler = logging.FileHandler(ERROR_FILENAME)
#    error_handler.setLevel(logging.ERROR)

    # Initializes a thread lock which can be used to serialize access
    # to underlying I/O functionality which may not be threadsafe.
#    handler.createLock()
#    error_handler.createLock()

    # Acquires the thread lock created with createLock().
#    handler.acquire()
#    error_handler.acquire()

    # Add the log message handlers to the logger
#    logger.addHandler(handler)
#    logger.addHandler(error_handler)

    addr_book = AddressBook()
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
        "name": "Mario",
        "address": ["via alfa", "via beta"],
        "email": ["mario.mario@gmail.com", "mario@gmail.com"],
        "phone": ["012345678", "8765431"],
        "groups": ["Alfa", "Gamma"]
    }
    person2 = Person(person_args)
    # Add a group to the address book.
    addr_book.add_group("Alfa")
    addr_book.add_group("Gamma")

    # Add a group to the address book.

    # Add a person to the address book.
    addr_book.add_person(person1)
    addr_book.add_person(person2)
    print("Persons:\n%s" % (addr_book.get_persons_str()))
    print("Groups:\n%s" % (addr_book.get_groups_str()))

    # Given a group we want to easily find its members
    for person in addr_book.get_group_members("Alfa"):
        print("Person: %s" % person.get_full_name())

    # Given a person we want to easily find the groups the person belongs to.
    print("Person: " + str(addr_book.get_person_group(person1)))

    # Find person by name (can supply either first name, last name, or both).
    persons_found = addr_book.find_person("Mario", "Luigi")
    if persons_found is not None:
        for person in persons_found:
            print(person.get_fmt_str())
    print("--------------------------")
    persons_found = addr_book.find_person("Mario")
    if persons_found is not None:
        for person in persons_found:
            print(person.get_fmt_str())
    print("--------------------------")
    persons_found = addr_book.find_person(None, "Luigi")
    if persons_found is not None:
        for person in persons_found:
            print(person.get_fmt_str())

    print("--------------------------")
    # Find person by email address (can supply either the exact string
    # or a prefix string,
    # ie. both "alexander@company.com" and "alex" should work).
    person_found = addr_book.find_person_by_email("luigi.riefolo@gmail.com")
    if person_found is not None:
        print("Found:\n%s" % person_found.get_fmt_str())

    person = addr_book.find_person_by_email("luigi")
    if person is not None:
        print("Person found")

if __name__ == "__main__":
    sys.exit(main())
