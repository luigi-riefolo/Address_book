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

    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone

    def getGroups(self):
        return self.groups

    def toStr(self):
        print("Lastname:\t\t%s\nName:\t\t\t%s" % 
            (self.lastname, self.name))
        sys.stdout.write("Address:")
        pad = ""
        for a in self.address:
            print("\t\t%s%s" % (pad, a))
            pad = "\t"

        sys.stdout.write("Email:")
        for a in self.email:
            print("\t\t\t%s" % (a))
        pad = ""

        sys.stdout.write("Phone:\t")
        for a in self.phone:
            print("\t\t%s%s" % (pad, a))
            pad = "\t"
        pad = ""

        sys.stdout.write("Groups:\t")
        if not len(self.groups):
            print("\t\tNone")
        for a in self.groups:
            print("\t\t%s%s" % (pad, a))
            pad = "\t"

