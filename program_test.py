from contacts_class import ContactAdd


def program_test():

    print("List of Contacts to be added\n")
    contact_1 = ContactAdd("Adam Clarke", "32 Privett Road", "343-222-3456", "12/05/1956")
    print(contact_1)
    contact_2 = ContactAdd("Brad Hood", "32 Privencial Road", "400-222-3456", "12/07/1956")
    print(contact_2)
    contact_3 = ContactAdd("Dame Slough", "32 Prince Road", "343-222-3456", "12/06/1956")
    print(contact_3)
    contact_4 = ContactAdd("Atriah Thums", "32 Private Road", "343-222-3456", "12/09/1956")
    print(contact_4)

    contact_1.save_contact()
    contact_2.save_contact()
    contact_3.save_contact()
    contact_4.save_contact()


program_test()
