# The functions need to access the csv file
import csv


# Returns the details of a specific Contact
def search_contact():

    choose_contact = input("\nSearch for specific Contact? Type Yes or No: ").title()
    if choose_contact == "Yes":
        specific_contact = input("Choose Contact by their: 'Name', 'Address', 'Phone', 'Birthday':").title()

        if specific_contact == "Name":

            name_to_search = input("What is the Name of the specific Contact? ")

            with open("stored_contacts.csv") as f:
                reader = csv.reader(f)

                found = False
                for line in reader:
                    if line[0] == name_to_search:
                        print(line)
                        found = True
                if not found:
                    print(name_to_search, "The name is not recognised")

        elif specific_contact == "Address":
            address_to_search = input("What is the Address of the specific Contact? ")

            with open("stored_contacts.csv") as e:
                reader = csv.reader(e)

                found = False
                for line in reader:
                    if line[1] == address_to_search:
                        print(line)
                        found = True
                if not found:
                    print(address_to_search, "The address is not recognised")
        elif specific_contact == "Phone":
            phone_to_search = input("What is the Phone number of the specific Contact? ")

            with open("stored_contacts.csv") as p:
                reader = csv.reader(p)

                found = False
                for line in reader:
                    if line[2] == phone_to_search:
                        print(line)
                        found = True
                if not found:
                    print(phone_to_search, "Phone number is not recognised")
        elif specific_contact == "Birthday":
            birthday_to_search = input("What is the Birthday of the specific Contact? ")

            with open("stored_contacts.csv") as b:
                reader = csv.reader(b)

                found = False
                for line in reader:
                    if line[3] == birthday_to_search:
                        print(line)
                        found = True
                if not found:
                    print(birthday_to_search, "The birthday is not recognised")
        else:
            print("Did not understand the input")
    else:
        print("Did not choose to search for a specific Contact")


# Returns the details of all Contacts
def print_contacts():

    show_contacts = input("\nSee all Contacts? Type Yes or No: ").title()
    if show_contacts == "Yes":
        with open('stored_contacts.csv', 'rt')as f:
            data = csv.reader(f)
            for row in data:
                print(row)
    else:
        print('Chose not to see all contacts')


# Deletes a specific contact based on input of name
def del_contact():

    delete_contact = input("\nDelete a Specific Contact? Type Yes or No: ").title()
    if delete_contact == "Yes":
        find_name = input('Enter the Name of the Contact you want to delete: ').title()
        with open('stored_contacts.csv', 'r') as d:

            contact = d.readlines()
        name_found = [x for x in contact if x.split(',')[0].lower() == find_name.lower()]
        if name_found:
            print('Remove the Contact: {}'.format(find_name))
            contact.remove(name_found[0])
            with open('stored_contacts.csv', 'w') as d:
                d.write(''.join(contact))
        else:
            print('Sorry! Name "{}" not found.'.format(find_name))
    else:
        print("Did not choose to delete a Contact")


# Edits the details of a previous Contact
def change_contact():

    my_list = []

    with open("stored_contacts.csv", "r") as file:
        the_file = csv.reader(file)
        for row in the_file:
            my_list.append(row)

        edit_row = ""
        edit_contact = input("\nEdit a Specific Contact? Type Yes or No: ").title()
        if edit_contact == "Yes":
            while True:

                try:
                    edit_row = int(input("Which Contact would you like to change? Enter 1-" + str(len(my_list)-1)+" :"))
                    break
                except ValueError:
                    print("Sorry I didn't understand that")
                    continue

            print("Please enter the new details for each of the following : ")

            for i in range(len(my_list[0])):
                new_contact_details = input("Enter the new data for " + str(my_list[0][i] + " :"))
                my_list[edit_row][i] = new_contact_details

            change_csv = input("\nWould you like to make changes to the csv file? Type Yes or No: ").lower()

            if change_csv == "yes":
                with open("stored_contacts.csv", "w", newline='') as file:

                    the_file = csv.writer(file)
                    for i in range(len(my_list)):
                        the_file.writerow(my_list[i])
        else:
            print("Did not choose to edit a Contact")

    print("\nThe program has finished")
