#!/usr/bin/env python

"""
A person class.
"""


class Person(object):

    """
    A person representation.

    Attributes:
        name: A string representing a Person's name
        lastname: A string representing a Person's lastname
        address: An array of strings representing one or more street addresses
        email: An array of strings representing one or more email addresses
        phone: An array of strings representing one or more phone numbers
        groups: An array of strings representing one or more Person's groups
    """

    def __init__(self, args):
        self.lastname = args["lastname"]
        self.name = args["name"]
        self.address = args["address"]
        self.email = args["email"]
        self.phone = args["phone"]
        self.groups = args["groups"]

    def set_address(self, address):
        """ Set a list of addresses """
        self.address = address

    def set_email(self, email):
        """ Set a list of emails """
        self.email = email

    def set_phone(self, phone):
        """ Set a list of phone numbers """
        self.phone = phone

    def set_groups(self, groups):
        """ Set a list of groups """
        self.groups = groups

    def get_name(self):
        """ Get person's name """
        return self.name

    def get_lastname(self):
        """ Get person's lastname """
        return self.lastname

    def get_full_name(self):
        """ Get person's fullname """
        return self.lastname + " " + self.name

    def get_full_name_code(self):
        """ Get person's fullname code """
        return self.lastname + "_" + self.name

    def get_address(self):
        """ Get person's address list """
        return self.address

    def get_email(self):
        """ Get person's emails list """
        return self.email

    def get_phone(self):
        """ Get person's phone numbers list """
        return self.phone

    def get_groups(self):
        """ Get person's groups list """
        return self.groups

    def __str__(self):
        person = (
            "lastname: {0}, "
            "name: {1}, "
            "address: {2}, "
            "email: {3}, "
            "phone: {4}, "
            "group: {5}"
        ).format(
            self.lastname,
            self.name,
            self.address,
            self.email,
            self.phone,
            self.groups)

        return person

    def get_fmt_str(self):
        """ Create a person formatted string representation """
        person = "Lastname:\t\t{0}\n".format(self.lastname)
        person += "Name:\t\t\t{0}\n".format(self.name)
        person += "Address:\t\t"
        person += str.join(", ", self.address)
        person += "\n"

        person += "Email:\t\t\t"
        person += str.join(", ", self.email)
        person += "\n"

        person += "Phone:\t\t\t"
        person += str.join(", ", self.phone)
        person += "\n"

        person += "Groups:\t\t\t"
        person += str.join(", ", self.groups)
        person += "\n"

        return person
