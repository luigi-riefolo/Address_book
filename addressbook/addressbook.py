#!/usr/bin/env python

import re
import sys
import addressbook
import logging

class AddressBook:
    """
    An address book class

    Attributes:
        persons: A dict containing a collection of persons
        groups: A dict containing a collection of groups
        emails: A dict containing a collection of persons' email addresses
    """

    def __init__(self):
        logging.info("New address book created")
        self.numbers = dict()
        self.persons = dict()
        self.groups = dict()
        self.emails = dict()

    # Add a person to the address book
    # NOTE:
    # The person's phone numbers are
    # used as keys in the address book, as
    # multiple persons with the same name
    # and lastname cannot have the same 
    # phone number
    def addPerson(self, person):
        fullName = person.getFullNameCode()
        if fullName not in self.persons:
            self.persons[fullName] = []
 
        logging.info("Adding new person: %s" % (person.getFullName()))

        self.persons[fullName].append(person)

        for num in person.getPhone():
            self.numbers[num] = person

        for email in person.getEmail():
            self.emails[email] = person

        for group in person.getGroups():
            if group in self.groups:
                self.groups[group].append(person)


    # Reports whether a group is in the address book
    def groupExists(self, group):
        print("GROUP: " + group)
        if group in self.groups:
            return True

        return False


    # Add a group to the address book
    def addGroup(self, group):
        logging.info("Adding group '%s'" % (group))
        if self.groupExists(group):
            logging.info("Group '%s' already exists" % (group))
        else:
            self.groups[group] = []


    # Get a group's list of members
    def getGroupMembers(self, group):
        logging.info("Getting group members for '%s'" % (group))
        if self.groupExists(group):
            return self.groups[group]
        else:
            logging.warning("Group '%s' does not exist" % (group))
            return None


    # Reports whether a person is in the address book
    def personExists(self, fullName):
        if fullName in self.persons:
            return True
        else:
            return False


    # Get person's list of groups
    def getPersonGroup(self, person):
        fullName = person.getFullNameCode()
        if not self.personExists(fullName):
            return None

        groups = dict()
        for person in self.persons[fullName]:
            groups[person.getFullName()] = person.getGroups()
        return groups


    def getFullNameCode(self, lastname, name):
        return lastname + "_" + name


    # Find a list of persons by name, supplying 
    # either first name, last name, or both
    def findPerson(self, lastname, name):
        persons = None

        if name != None and lastname != None:
            fullName = self.getFullNameCode(lastname, name)
            if self.personExists(fullName):
                persons = self.persons[fullName] 

        elif name != None or lastname != None:
            reg = None

            if name != None and lastname == None:
                reg = re.compile(r'^[\w-]+_%s$' % (name))
            if name == None and lastname != None:
                reg = re.compile(r'%s_' % (lastname))
            
            for fullName, personList in self.persons.iteritems():
                if re.match(reg, fullName):
                    persons = personList
 
        if persons == None:    
            logging.warning("Could not find requested person")

        return persons
     
   
    # Find person by email address, supplying either 
    # the exact string or a prefix string, 
    # ie. both "alexander@company.com" and "alex" should work.
    def findPersonByEmail(self, email):
        r = re.compile(r'.+@.+')
        emailRe = None
        if re.match(r, email):
            emailRe = re.compile(email)
        else:
            emailRe = re.compile(r'%s.*@.+\.-{2,5}' % (email))

        for fullName, persons in self.persons.iteritems():
            for person in persons:
                for email in person.getEmail():
                    if re.match(emailRe, email):
                        return person

        return None

    
    def personsToStr(self):
        persons = []
        for fullName, personObj in self.persons.iteritems():
            for person in self.persons[fullName]:
                persons.append(person.toStr())

        return persons


    def groupsToStr(self):
        groups = []
        for group, members in self.groups.iteritems():
            groups.append(group)

        return groups
