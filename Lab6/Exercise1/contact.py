ALLOWED_PARAMETERS = ("name", "address", "birthday", "phone number", "email", "profession", "interests")


class Contact:
    """Class for creating, deleting and modifying contacts"""

    def __init__(self, name, phone_number, address="", birthday="", email="", profession="", interests=""):
        self.__name = name
        self.__address = address
        self.__birthday = birthday
        self.__phone_number = phone_number
        self.__email = email
        self.__profession = profession
        self.__interests = interests

    def __str__(self):
        return "name:{},address:{},birthday:{},phone number:{},email:{},profession:{},interests:{}"\
                .format(self.__name, self.__address, self.__birthday, self.__phone_number, self.__email,
                        self.__profession, self.__interests)

    @classmethod
    def parse(cls, input_str):
        contact_info_list = input_str.split(',')

        contacts_dict = {}
        for contact_info in contact_info_list:
            contact_parameter = contact_info.split(':')[0].strip().lower()
            contact_value = contact_info.split(':')[1].strip()

            if contact_parameter in ALLOWED_PARAMETERS:
                contacts_dict[contact_parameter] = contact_value

        return cls(name=contacts_dict["name"], phone_number=contacts_dict["phone number"],
                   address=contacts_dict["address"], birthday=contacts_dict["birthday"],
                   email=contacts_dict["email"], profession=contacts_dict["profession"],
                   interests=contacts_dict["interests"])

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_birthday(self):
        return self.__birthday

    def set_birthday(self, birthday):
        self.__birthday = birthday

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_profession(self):
        return self.__profession

    def set_profession(self, profession):
        self.__profession = profession

    def get_interests(self):
        return self.__interests

    def set_interests(self, interests):
        self.__interests = interests

    def create_entry(self):
        with open("contacts.txt", mode='a', encoding='utf-8') as file:
            string_to_write = str(self)

            file.write(string_to_write + "\n")

    @staticmethod
    def search_entries(input_str):
        parameter = input_str.split(':')[0].strip().lower()
        value = input_str.split(':')[1].strip()

        matching_contacts = []

        if parameter in ALLOWED_PARAMETERS:
            with open("contacts.txt", mode='r', encoding='utf-8') as file:
                current_line = ' '
                while current_line != '':
                    current_line = file.readline()

                    if parameter + ":" + value in current_line:
                        matching_contacts.append(Contact.parse(current_line))
        else:
            print("Invalid parameter!")
            return

        return matching_contacts

    @staticmethod
    def remove_entry(contact_to_remove):

        with open("contacts.txt", "r") as file:
            lines = file.readlines()
        with open("contacts.txt", "w") as file:
            is_removed = False
            for line in lines:
                if line.strip("\n") == str(contact_to_remove).strip("\n") and is_removed == False:
                    is_removed = True
                else:
                    file.write(line)

    def update_entry(self, new_contact):

        with open("contacts.txt", "r") as file:
            lines = file.readlines()
        with open("contacts.txt", "w") as file:
            is_changed = False
            for line in lines:
                if line.strip("\n") == str(self).strip("\n") and is_changed == False:
                    file.write(str(new_contact) + "\n")
                    is_changed = True
                else:
                    file.write(line)

    def update_parameter(self, parameter, value):
        updated_contact = Contact.parse(str(self))

        if parameter == "name":
            updated_contact.set_name(value)
        elif parameter == "address":
            updated_contact.set_address(value)
        elif parameter == "birthday":
            updated_contact.set_birthday(value)
        elif parameter == "phone number":
            updated_contact.set_phone_number(value)
        elif parameter == "email":
            updated_contact.set_email(value)
        elif parameter == "profession":
            updated_contact.set_profession(value)
        elif parameter == "interests":
            updated_contact.set_interests(value)
        else:
            print("The " + parameter + " parameter is not a valid input.")
            return

        return updated_contact