from contact import Contact

print("Welcome to your personal contact book.")

while True:
    print('''
    Your options are:

    1) Create a contact
    2) Update an existing contact
    3) Search for an existing contact
    4) Remove a contact
    5) Exit
                                            ''')
    try:
        user_choise = int(input("Choose your option: "))
    except:
        print("Not a valid input.")
        continue

    if user_choise == 1:
        contact_input = input("Type in the data in the format "
                              "(name: \"name\", address: \"address\", birthday: \"birthday\", "
                              "phone number: \"phone number\", email: \"email\", "
                              "profession: \"profession\", interests: \"interests\"): ")

        contact = Contact(name="", phone_number="")

        contact_info_list = contact_input.split(',')

        for contact_info in contact_info_list:
            contact_parameter = contact_info.split(':')[0].strip().lower()
            contact_value = contact_info.split(':')[1].strip()

            contact = contact.update_parameter(contact_parameter, contact_value)

        if contact.get_name() == "" or contact.get_phone_number() == "":
            print("Your input must contain name parameter and phone number parameter.")
            continue

        contact.create_entry()

    elif user_choise == 2:
        user_input = input(
            "Search for a contact you want to update by what (example - name: \"the name you are searching for\"): ")

        matched_contacts = Contact.search_entries(user_input)

        index_to_change = 0
        if len(matched_contacts) == 0:
            print("There are no matching contacts")
            continue

        elif len(matched_contacts) > 1:
            print("There are " + str(len(matched_contacts)) + " contacts that match your criteria: ")

            for i in range(0, len(matched_contacts)):
                print("\t" + str(i + 1) + ") " + str(matched_contacts[i]))

            index_to_change = int(input("Which contact to change? ")) - 1

        info_to_change = input(
            "What would you want to change in the contact (example - name: \"changed name\"): ").split(":")
        parameter_to_change = info_to_change[0].strip()
        value_to_change = info_to_change[1].strip()

        old_contact = matched_contacts[index_to_change]

        new_contact = old_contact.update_parameter(parameter_to_change, value_to_change)

        old_contact.update_entry(new_contact)

    elif user_choise == 3:
        user_input = input("Search for a contact by what (example - name: \"the name you are searching for\"): ")

        matched_contacts = Contact.search_entries(user_input)

        print("There are " + str(len(matched_contacts)) + " contacts that match your criteria: \n")
        for i in range(0, len(matched_contacts)):
            print("\t" + str(i + 1) + ") " + str(matched_contacts[i]))

    elif user_choise == 4:
        user_input = input(
            "Search for a contact you want to remove by what (example - name: \"the name you are searching for\"): ")

        matched_contacts = Contact.search_entries(user_input)

        index_to_change = 0
        if len(matched_contacts) == 0:
            print("There are no matching contacts")
            continue

        elif len(matched_contacts) > 1:
            print("There are " + str(len(matched_contacts)) + " contacts that match your criteria: ")

            for i in range(0, len(matched_contacts)):
                print("\t" + str(i + 1) + ") " + str(matched_contacts[i]))

            index_to_change = int(input("Which contact to change? ")) - 1

        Contact.remove_entry(matched_contacts[index_to_change])

    elif user_choise == 5:
        break