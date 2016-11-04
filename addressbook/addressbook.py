#!/usr/bin/env python

"""
Adddress book API.
"""

from __future__ import print_function

import re
import logging


class AddressBook(object):
    """
    An address book class.

    Attributes:
        @param persons: Dict containing a collection of persons.
        @param groups: Dict containing a collection of groups
        @param emails: Dict containing a collection of email addresses.
    """
    def __init__(self):
        logging.info("New address book created")
        self.numbers = dict()
        self.persons = dict()
        self.groups = dict()
        self.emails = dict()

    def add_person(self, person):
        """
        Add a person to the address book.

        @param person: Person object to add.

        The person's phone numbers are
        used as keys in the address book, as
        multiple persons with the same name
        and lastname cannot have the same
        phone number.
        """
        full_name = person.get_full_name_code()
        if full_name not in self.persons:
            self.persons[full_name] = []

        logging.info("Adding new person: %s", person.get_full_name())

        self.persons[full_name].append(person)

        for num in person.get_phone():
            self.numbers[num] = person

        for email in person.get_email():
            self.emails[email] = person

        for group in person.get_groups():
            if group in self.groups:
                self.groups[group].append(person)

    def group_exists(self, group):
        """
        Reports whether a group is in the address book.

        @param group: The group to check.
        @return: Boolean.
        """
        if group in self.groups:
            return True

        return False

    def add_group(self, group):
        """
        Add a group to the address book.

        @param group: The group string to be added.
        """
        logging.info("Adding group '%s'", group)
        if self.group_exists(group):
            logging.info("Group '%s' already exists", group)
        else:
            self.groups[group] = []

    def get_group_members(self, group):
        """
        Get a group's list of members.

        @param group: Requested group.
        @return: List containing group members.
        """
        logging.info("Getting group members for '%s'", group)
        if self.group_exists(group):
            return self.groups[group]
        else:
            logging.warning("Group '%s' does not exist", group)
            return None

    def person_exists(self, full_name):
        """
        Reports whether a person is in the address book.

        @param full_name: Person's fullname.
        @return: Boolean
        """
        return bool(full_name in self.persons)

    def get_person_group(self, person):
        """
        Get person's list of groups.

        @param person: Requested person.
        @return: A list of groups or an empty dict.
        """
        full_name = person.get_full_name_code()
        if not self.person_exists(full_name):
            return None

        groups = dict()
        for person in self.persons[full_name]:
            groups[person.get_full_name()] = person.get_groups()
        return groups

    @staticmethod
    def get_full_name_code(lastname, name):
        """
        Return a fullname code.

        @param lastname: Person's lastname.
        @param name: Person's name.
        @return: A string containing a fullname code.
        """
        return lastname + "_" + name

    def find_person(self, lastname=None, name=None):
        """
        Find a list of persons by name.

        @param lastname: Person's lastname.
        @param name: Person's name.

        @return: A list of person objects or None.

        Supplying either first name, last name, or both.
        """
        persons = None

        if name is not None and lastname is not None:
            full_name = self.get_full_name_code(lastname, name)
            if self.person_exists(full_name):
                persons = self.persons[full_name]

        elif name is not None or lastname is not None:
            reg = None

            if name is not None and lastname is None:
                reg = re.compile(r'^[\w-]+_%s$' % (name))
            if name is None and lastname is not None:
                reg = re.compile(r'%s_' % (lastname))

            for full_name, person_list in self.persons.iteritems():
                if re.match(reg, full_name):
                    persons = person_list

        if persons is None:
            logging.warning("Could not find requested person")
        else:
            logging.info("Requested person found")

        return persons

    def find_person_by_email(self, email):
        """
        Find person by email address.

        @param email: Person's email.
        @return: A person object or None.

        Supplying either the exact string or a prefix string,
        ie. both "alexander@company.com" and "alex" are valid patterns.
        """
        email_re = re.compile(r'.+@.+')
        full_email_re = None
        if re.match(email_re, email):
            full_email_re = re.compile(email)
        else:
            full_email_re = re.compile(r'.*%s.*@.+\..{2,5}' % (email))

        print("FIND: " + email)
        for email, person in self.emails.iteritems():
            print("EMAIL: " + email)
            if re.match(full_email_re, email):
                logging.info("Requested person found")
                return person

        logging.warning("Could not find requested person")

        return None

    def get_persons_str(self):
        """
        Return a person's string representation.

        @return: A string representation of a person object.
        """
        persons = ""
        for full_name, _ in self.persons.iteritems():
            for person in self.persons[full_name]:
                persons += person.get_fmt_str()
                persons += '-' * 20 + "\n"

        return persons

    def get_groups_str(self):
        """
        Return a group's string representation.

        @return: A string representation of a group object.
        """
        groups = ""
        for group, _ in self.groups.iteritems():
            groups += str(group)
            groups += '\n' + '-' * 20 + "\n"

        return groups
