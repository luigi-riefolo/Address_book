#!/usr/bin/env python

import re
import sys

class AddressBook:
    """
    An address book class

    Attributes:
        persons: A dict containing a collection of persons
        groups: A dict containing a collection of groups
        emails: A dict containing a collection of persons' email addresses
    """

    def __init__(self):
        self.numbers = dict()
        self.persons = dict()
        self.groups = dict()
        self.emails = dict()
        self.personNo = 0

    # Add a person to the address book
    # NOTE:
    # The person's phone numbers are
    # used as keys in the address book, as
    # multiple persons with the same name
    # and lastname cannot have the same 
    # phone number
    def addPerson(self, person):
        k = person.getLastname() + "_" + person.getName()
        if k not in self.persons:
            self.persons[k] = []
        self.persons[k].append(person)

        for n in person.getPhone():
            self.numbers[n] = person

        for e in person.getEmail():
            self.emails[e] = person

        for g in person.getGroups():
            if g in self.groups:
                self.groups[g].append(person)
        self.personNo += 1


    # Add a group to the address book
    def addGroup(self, group):
        self.groups[group] = []

    # Get a group's list of members
    def getGroupMembers(self, group):
        return self.groups[group]
    
    # Get person's list of groups
    def getPersonGroup(self, person):
        k = person.getLastname() + "_" + person.getName()
        ret = dict()
        for p in self.persons[k]:
            ret[p.getFullName()] = p.getGroups()
        return ret
    
    # Find person by name, supplying either 
    # first name, last name, or both
    def findPerson(self, lastname, name):
        p = None
        if name != None and lastname != None:
            k = lastname + "_" + name
            p = self.persons[k] 

        elif name != None or lastname != None:
            reg = None

            if name != None and lastname == None:
                reg = re.compile(r'^[\w-]+_%s$' % (name))
            if name == None and lastname != None:
                reg = re.compile(r'%s_' % (lastname))
            
            for k, v in self.persons.iteritems():
                if re.match(reg, k):
                    p = v
 
        if p == None:    
            print("Could not find requested person")

        return p
     
   
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

        p = None
        for k, v in self.persons.iteritems():
            for p in v:
                for e in p.getEmail():
                    if re.match(emailRe, e):
                        p = v
        return p

    sep = "------------------------------------"
    
    def personsToStr(self):
        print("Persons in address book (%s):" % self.personNo)
        for k, v in self.persons.iteritems():
            for p in self.persons[k]:
                p.toStr()
                print(self.sep)

    def groupsToStr(self):
        print("Groups in address book (%s)" % (len(self.groups)))
        for k, v in self.groups.iteritems():
            sys.stdout.write("%s:\t\t" % (k))
            if not len(v):
                print("\tEmpty")
            pad = ""
            for p in v:
                print("\t%s%s" % (pad, p.getFullName()))
                pad = "\t\t"
            print(self.sep)

