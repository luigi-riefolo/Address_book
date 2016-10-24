#from unittest import TestCase
import unittest
from addressbook import AddressBook, Person


class TestPerson(unittest.TestCase):
    g1 = "Alfa"
    g2 = "Gamma"
    p1 = Person(
        "Luigi",
        "Mario",
        ["via alfa", "via beta"],
        ["luigi.mario@gmail.com", "luigi@gmail.com"],
        ["012345678", "8765431"],
        ["Alfa", "Gamma"]) 
    p2 = Person(
        "Mario",
        "Mario",
        ["via alfa", "via beta"],
        ["mario.mario@gmail.com", "mario@gmail.com"],
        ["012345678", "8765431"],
        ["Alfa", "Gamma"]) 

    # Add a group to the address book
    def test_add_person(self):
        ab = AddressBook()
        ab.addPerson(self.p1)        
        k = self.p1.getLastname() + "_" + self.p1.getName()
        self.assertTrue(k in ab.persons)

    def test_person_not_in_address_book(self):
        ab = AddressBook()
        k = "Mario_Luigi"
        self.assertFalse(k in ab.persons)

    # Add a group to the address book.      
    def test_add_group(self):
        ab = AddressBook()
        ab.addGroup(self.g1)                      
        self.assertTrue(self.g1 in ab.groups)

    # Given a group we want to easily find its members
    def test_find_group_members(self):
        ab = AddressBook()
        ab.addGroup(self.g2)
        ab.addPerson(self.p1)   
        ab.addPerson(self.p2)   
        for g in ab.getGroupMembers(self.g2):
            print("Person: " + g.getFullName())
            self.assertTrue(isinstance(g.getFullName(), basestring))
       
    # Given a person we want to easily find the groups the person belongs to
    def test_get_person_groups(self):
        ab = AddressBook()
        ab.addGroup(self.g2)
        ab.addPerson(self.p1)
        groups = ab.getPersonGroup(self.p1)
        self.assertIsNotNone(groups)
        print("Groups: " + str(groups)) 
        
    # Find person by name (can supply either first name, last name, or both).
    def test_find_person_by_fullname(self):
        ab = AddressBook()
        ab.addPerson(self.p1)
        a = ab.findPerson("Mario", "Luigi")
        self.assertIsNotNone(a)
        for t in a:
            t.toStr()
    
    def test_find_person_by_lastname(self):
        ab = AddressBook()
        ab.addPerson(self.p1)
        b = ab.findPerson("Mario", None)
        self.assertIsNotNone(b)
        for t in b:
            t.toStr()

    def test_find_person_by_name(self):
        ab = AddressBook()
        ab.addPerson(self.p1)
        c = ab.findPerson(None, "Luigi")
        self.assertIsNotNone(c)
        for t in c:
            t.toStr()
        
    # Find person by email address, supplying either the exact 
    # string or a prefix string, ie. both 
    # "alexander@company.com" and "alex" should work).
    def test_find_person_by_email(self):
        ab = AddressBook()
        ab.addPerson(self.p1)
        d = ab.findPersonByEmail("luigi.mario@gmail.com")
        self.assertIsNotNone(d)
        print("Person found")    

    def test_find_person_by_partial_email(self):
        ab = AddressBook()
        ab.addPerson(self.p1)
        e = ab.findPersonByEmail("luigi")
        self.assertIsNotNone(e)
        print("Person found")    


if __name__ == '__main__':
    unittest.main()
