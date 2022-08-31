# Description for HW-11

This is a package with 1 module for dealing with user's contact book with using of classes.
Was prepared as a homework for unit 11 of Python core course in CoIT school.

Contain classes:  
 - AddressBook (which inherits from UserDict)
 - Record (which is responsible for the logic of adding/removing/editing optional fields and storing the mandatory field Name)
 - Field (which will be the parent of all fields)
 - Name (required field with name), Phone (optional field with phone number) and Birthday (optional field with date of birth)

To Phone and Birthday were added setters.
To Record was added function to count days to nearest birthday.
To AddressBook was added pagination iterator.


Main package with module is located here  
https://github.com/AndriiBobanych/goit_classes_phonebook_assistance_v2


Author: <b>Andrii Bobanych<b>