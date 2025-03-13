# Class
class ContactAdd:

    # Constructor
    def __init__(self, name, address, phone, birthday):
        # __ makes variables/attributes private
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__birthday = birthday

    def __repr__(self):
        return f"[{self.__name},{self.__address},{self.__phone},{self.__address}]"

    # Class methods
    # Return the details of the new Contact
    def add_contact(self):

        print(f'''The details are:
                Name: {self.__name}
                Address: {self.__address}
                Phone: {self.__phone}
                Birthday: {self.__birthday}
                ''')

    # Saves the details of the new Contact
    def save_contact(self):
        pass

        save = input("\nWould you like to save this Contact? Type Yes or No: ").lower()

        if save == "yes":
            f = open("stored_contacts.csv", "a")
            f.write(f"{self.__name}, {self.__address}, {self.__phone}, {self.__birthday}\n")

            f.close()
            print("Contact Saved!")
        else:
            print("Contact not saved")
