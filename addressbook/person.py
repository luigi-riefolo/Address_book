#!/usr/bin/env python

import sys


class Person:
    """
    A person class
    
    Attributes:
        name: A string representing a Person's name
        lastname: A string representing a Person's lastname
        address: An array of strings representing one or more street addresses
        email: An array of strings representing one or more email addresses
        phone: An array of strings representing one or more phone numbers
        groups: An array of strings representing one or more Person's groups
    """
    def __init__(self, name, lastname, address, email, phone, groups):
        self.name = name
        self.lastname = lastname
        self.address = address
        self.email = email
        self.phone = phone
        self.groups = groups

    # Setters
    def setAddress(self, address):
        self.address = address

    def setEmail(self, email):
        self.email = email

    def setPhone(self, phone):
        self.phone = phone

    def setGroups(self, groups):
        self.groups = groups

    # Getters 
    def getName(self):
        return self.name
    
    def getLastname(self):
        return self.lastname

    def getFullName(self):
        return self.lastname + " " + self.name

    def getFullNameCode(self):
        return self.lastname + "_" + self.name

    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone

    def getGroups(self):
        return self.groups

    def toStr(self):
        person = (
            "lastname: {0}, "
            "name: {1}, "
            "address: {2}, "
            "email: {3}, "
            "phone: {4}, "
            "group: {5}"
        ).format(self.lastname, self.name, self.address, self.email, self.phone, self.groups)

        return person


    def toFmtStr(self):
        person = "Lastname:\t\t{0}\nName:\t\t\t{1}\n".format(self.lastname, self.name)
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

