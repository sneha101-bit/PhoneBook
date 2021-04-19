# Define a function to welcome user and provide options on which phonebook works
def welcome():
    entry = int(input('''
Welcome to PhoneBook!!!
What would you like to do?
1. Display existing contacts
2. Create new contact
3. Check an entry
4. Delete an entry
5. Exit
Enter your entry here(1, 2, 3, 4 OR 5):
'''))
    return entry

# Define main function phonebook
def phonebook():
    contact = {}

    while True:
        entry = welcome()

        if entry == 1:
            if bool(contact) != False:
                for con_no, con_name in contact.items():
                    print(con_name, con_no)
            else:
                print("Your PhoneBook is empty, go back to menu to add new contact")
        elif entry == 2:
            con_no = int(input("Please enter Contact Number: "))
            con_name = input("Please enter Contact Name in the format 'FirstName, LastName': ")
            if con_no not in contact.items():
                contact.update({con_name:con_no})
                print("Contacts updated successfully")
                print("Updated PhoneBook is shown below: ")
                for con_name, con_no in contact.items():
                    print(f"{con_name} : {con_no}")
            else:
                print("Contact no. already exists in the PhoneBook")
        elif entry == 3:
            con_name = input("Please enter contact name which you want to wish to view: ")
            if con_name in contact:
                print(f"{con_name} : {contact[con_name]}")
            else:
                print("This no. does not exists, go back to menu to add contact")
        elif entry == 4:
            con_name = input("Please enter contact name which you want to wish to delete: ")
            if con_name in contact:
                print(f"{con_name} : {contact[con_name]}")

            confirm = input('Do you really want to delete this entry?(YES/NO)')

            if confirm == 'YES':
                contact.pop(con_name,None)
                print("Updated PhoneBook is shown below: ")
                for con_name, con_no in contact.items():
                    print(f"{con_name} : {con_no}")
            else:
                print('Return to main menu')
        elif entry == 5:
            print("Thanks for using PhoneBook")
            break
        else:
            print('Incorrect Entry!')

phonebook()