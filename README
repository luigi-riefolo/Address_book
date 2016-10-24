Address Book API

INSTALLATION

	The Address Book API can be installed executing the following commands:

		cd addressbook/addressbook
		pip install .


USAGE

	Once installed the API can be used by just importing it:

		from addressbook import AddressBook, Person
		ab = AddressBook()

	Here's a few examples on how to use the API:

    	# Add a person to the address book.
    	p = Person(
            "Luigi",
            "Mario",
            ["via alfa", "via beta"],
            ["luigi.mario@gmail.com", "luigi@gmail.com"],
            ["012345678", "8765431"],
            ["Alfa", "Gamma"])
    	ab.addPerson(p)
    	
    	# Add a group to the address book.
    	ab.addGroup("Alfa")
    	ab.groupsToStr()
    
    	# Print address book content
    	ab.personsToStr()
    	ab.groupsToStr()
    
    	# Find list of person by lastname only
    	b = ab.findPerson("Mario", None)
    	if b is not None:
	 	for t in b:
			t.toStr()

	# Given a group we want to easily find its members
	for g in ab.getGroupMembers("Alfa"):
		print("P: " + g.getFullName())

	# Given a person we want to easily find the groups the person belongs to.
	print("G: " + str(ab.getPersonGroup(p)))   

	# Find person by email address, supplying either the exact 
	# string or a prefix string, ie. both "alexander@company.com" 
	# and "alex" should work).
	d = ab.findPersonByEmail("luigi.riefolo@gmail.com")
	if d is not None:
		for p in d:
			p.toStr()

 
TESTING

	All API calls are unit-tested, to run the unit-tests:

		cd addressbook/addressbook/tests/
		python test_address_book.py 


DESIGN

	How would you find a person by their email address, supplying any substring, 
	ie. "comp" should find "alexander@company.com":

	- Using a regex we can find any email address that matches the pattern
	- An address book can store a collection of email addresses in a dict, as they're all unique
	- Looping through the dict and matching against the requested pattern would return a list of persons

	If we want to improve performances then we should use advanced data structures such as Tries or
	Suffix Trees.
	Using the above we can store all combinations of emails and retrieve the list of persons more efficiently.


AUTHOR

	Luigi Riefolo <luigi.riefolo@gmail.com>


LICENSE

	This project does not require any license and it's free to use.

