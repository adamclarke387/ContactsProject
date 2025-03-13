# imports classes and functions from other python files
from contacts_class import ContactAdd
from class_manager import print_contacts, search_contact, del_contact, change_contact


# the main function which calls other functions
def main():
    # c = ContactAdd("") holds the data of the Contact the user wants to create
    c = ContactAdd("Adam Clarke", "34 Lowe avenue", " 868-575-2345", "12/12/1987")
    c.add_contact()
    c.save_contact()
    print_contacts()
    search_contact()
    del_contact()
    change_contact()


# if name equals main then run the main function
if __name__ == '__main__':
    main()
