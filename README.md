Address Book API

INSTALLATION

	The Address Book API can be installed executing the following commands:

		cd addressbook/addressbook
		pip install --upgrade .

	Or use the make file:

		make all

USAGE

	Once installed the API can be used by just importing it:

		from addressbook import AddressBook, Person

    Create an address book:

		addr_book = AddressBook()

	Create a person object and add it to the address book:

    	person_args = {
            "lastname": "Mario",
            "name": "Luigi",
            "address": ["via alfa", "via beta"],
            "email": ["luigi.mario@gmail.com", "luigi@gmail.com"],
            "phone": ["012345678", "8765431"],
            "groups": ["Alfa", "Gamma"]
        }
		person = Person(person_args)
		addr_book.add_person(person)

	Create a group and add it to the address book:

		addr_book.add_group("Alfa")

	Print the list of persons in the address book:

		print("Persons:\n%s" % (addr_book.get_persons_str()))

	Given a group we want to easily find its members

		for person in addr_book.get_group_members("Alfa"):
        	print("Person: %s" % person.get_full_name())

	Given a person we want to easily find the groups the person belongs to.
    	print("Person: " + str(addr_book.get_person_group(person)))

	Find a list of persons by name (user can supply either first name, last name, or both).

    	persons_found = addr_book.find_person("Mario", "Luigi")
    	if persons_found is not None:
        	for person in persons_found:
            	print(person.get_fmt_str())

		persons_found = addr_book.find_person("Mario")
        if persons_found is not None:
            for person in persons_found:
                print(person.get_fmt_str())

        persons_found = addr_book.find_person(None, "Luigi")
        if persons_found is not None:
            for person in persons_found:
                print(person.get_fmt_str())

	Given a group we want to easily find its members
		for person in addr_book.getGroupMembers("Alfa"):
			print("Person: " + person.get_full_name())


	Find person by email address, supplying either the exact string or
	a prefix string, ie. both "alexander@company.com" and "alex" should work).

		person_found = addr_book.find_person_by_email("luigi.riefolo@gmail.com")
    	if person_found is not None:
        	print("Found:\n%s" % person_found.get_fmt_str())


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


