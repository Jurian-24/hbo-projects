'''
Create an application that manages contacts in an addressbook. The following requirements should be implemented:
- Add a contact with first name and last name (only alphabet), multiple (unique) e-mails (containing at least one '@'),
  multiple (unique) phone numbers (only digits). Also, an ID should be generated which should be 1 higher than the highest current ID.
- Remove a contact by ID.
- List all contacts with the option to sort by first_name or last_name (default first_name) with a sort_by parameter
  and in ascending (ASC) or decending (DESC) direction (default ASC) witb a direction parameter.
- Merge duplicate contacts (automatically). Contacts with the exact same full name (first and last name combined) should be merged.
  The e-mails and phone numbers of the duplicate contacts should be added to the the first duplicate contact (contact with the highest ID).
  The other duplicate contcts should be deleted from the addressbook.
- Contacts are read from the provided JSON file and should be updated with new or removed contacts.
'''

import os
import sys
import json

addressbook = []

# Helpers


def emailCheck(email):
    for char in email:
        if char == '@':
            return True

    return False


def phoneCheck(phoneNumber):
    if (len(phoneNumber) >= 9):
        return phoneNumber.isdigit()

def removeArrayBrackets(string):
    string = str(string).replace("[", '')
    string = str(string).replace("]", '')
    string = str(string).replace("'", '')

    return string

'''
print all contacts in the following format:
======================================
Position: <position>
First name: <firstname>
Last name: <lastname>
Emails: <email_1>, <email_2>
Phone numbers: <number_1>, <number_2>
'''


def display(contactList, singleContact=None):
    if singleContact:
        print(f'Position: {contactList["id"]}')
        print(f'First name: {contactList["first_name"]}')
        print(f'Last name: {contactList["last_name"]}')
        print(f'Emails: {removeArrayBrackets(contactList["emails"])}')
        print(f'Phone numbers: {removeArrayBrackets(contactList["phone_numbers"])}')

    else:
        for contact in contactList:
            print(contact)
            print(f'Position: {contact["id"]}')
            print(f'First name: {contact["first_name"]}')
            print(f'Last name: {contact["last_name"]}')
            print(f'Emails: {removeArrayBrackets(contact["emails"])}')
            print(f'Phone numbers: {removeArrayBrackets(contact["phone_numbers"])}')
            print('\n')


'''
return list of contacts sorted by first_name or last_name [if blank then unsorted], direction [ASC (default)/DESC])
'''


def list_contacts():

    return display(addressbook)

'''
add new contact:
- first_name
- last_name
- emails = {}
- phone_numbers = {}
'''


def add_contact():

    firstName = input('').capitalize()
    lastName = input('').capitalize()
    emails = input('')
    phoneNumbers = input('')

    emails = emails.split(',')

    if len(emails) != len(set(emails)):
        return 'You cant enter the same email adress'

    emailInvalid = True
    while emailInvalid:
        for email in emails:
            if emailCheck(email):
                emailInvalid = False
            else:
                emails = input('Enter valid email adresses: ')

    emailAdresses = [emails]

    phoneNumbers = phoneNumbers.split(',')

    phonesInvalid = True
    while phonesInvalid:
        for phone in phoneNumbers:
            if phoneCheck(phone):
                phonesInvalid = False
            else:
                phoneNumbers = input('Enter valid phone numbers: ')

    newContact = {
        "id": len(addressbook) + 1,
        "first_name": firstName,
        "last_name": lastName,
        "emails": emails,
        "phone_numbers": phoneNumbers
    }

    addressbook.append(newContact)

    write_to_json('contacts.json')

    display(newContact, True)
'''
remove contact by ID (integer)
'''


def remove_contact():
    contactId = int(input('Which contact do you want remove'))

    for i in range(len(addressbook)):
        if addressbook[i]['id'] == contactId:
            addressbook.pop(i)
            break

    write_to_json('contacts.json')

'''
merge duplicates (automated > same fullname [firstname & lastname])
'''


def merge_contacts():
    # todo: implement this function
    ...


'''
read_from_json
Do NOT change this function
'''


def read_from_json(filename):
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in data:
            addressbook.append(contact)


'''
write_to_json
Do NOT change this function
'''


def write_to_json(filename):
    json_object = json.dumps(addressbook, indent=4)

    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


'''
main function:
# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [L] List contacts
# [A] Add contact
# [R] Remove contact
# [M] Merge contacts
# [Q] Quit program
Don't forget to put the contacts.json file in the same location as this file!
'''


def main(json_file):
    read_from_json(json_file)

    options = ['[L] List contacts', '[A] Add contact',
               '[R] Remove contact', '[M] Merge contacts', '[Q] Quit program', ]

    for option in options:
        print(option)

    choice = input('').lower()

    if choice == 'l':
        list_contacts()
        main('contacts.json')
    elif choice == 'a':
        add_contact()
        main('contacts.json')
    elif choice == 'r':
        remove_contact()
        main('contacts.json')
    elif choice == 'm':
        return True
    elif choice == 'q':
        return True
    else:
        main('contacts.json')


'''
calling main function::
Do NOT change it.
'''
if __name__ == "__main__":
    main('contacts.json')
