import contact_utilities as contact

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
        contacts_info = input("Type in the data in the format "
                              "(name: \"name\", address: \"address\", birthday: \"birthday\", "
                              "phone number: \"phone number\", email: \"email\", "
                              "profession: \"profession\", interests: \"interests\"): ")

        contact.create(contacts_info)

    elif user_choise == 2:
        user_input = input("Search for a contact you want to update by what (example - name: \"the name you are searching for\"): ")

        contacts_list = contact.search(user_input)
        str_to_change = ""
        index_to_change = 1

        if len(contacts_list) == 0:
            print("There are no matching contacts")
            continue

        elif len(contacts_list) > 1:
            print("There are " + str(len(contacts_list)) + " contacts that match your criteria: ")

            for i in range(0, len(contacts_list)):
                print("\t" + str(i + 1) + ") " + contacts_list[i])

            index_to_change = int(input("Which contact to change? "))


        info_to_change = input("What would you want to change in the contact (example - name: \"changed name\"): ").split(":")
        parameter_to_change = info_to_change[0].strip()
        value_to_change = info_to_change[1].strip()

        contact_to_change = {}
        for parameter_info_pair in contacts_list[index_to_change - 1].split(','):
            parameter = parameter_info_pair.split(':')[0].strip()
            info = parameter_info_pair.split(':')[1].strip()

            contact_to_change[parameter] = info

        if parameter_to_change == "name" or parameter_to_change == "address" or parameter_to_change == "birthday" or parameter_to_change == "phone number" or parameter_to_change == "email" or parameter_to_change == "profession" or parameter_to_change == "interests":
            contact_to_change[parameter_to_change] = value_to_change
        else:
            print("Not a valid parameter")
            continue

        for key, val in contact_to_change.items():
            str_to_change += key + ":" + val + ","
        contact.change_entry(contacts_list[index_to_change - 1], str_to_change.strip(','))


    elif user_choise == 3:
        user_input = input("Search for a contact by what (example - name: \"the name you are searching for\"): ")

        contacts_list = contact.search(user_input)

        print("There are " + str(len(contacts_list)) + " contacts that match your criteria: \n")
        for i in range(0, len(contacts_list)):
            print("\t" + str(i + 1) + ") " + contacts_list[i])

    elif user_choise == 4:
        user_input = input("Search for a contact you want to remove by what (example - name: \"the name you are searching for\"): ")
        contacts_list = contact.search(user_input)

        print("There are " + str(len(contacts_list)) + " contacts that match your criteria: \n")
        for i in range(0, len(contacts_list)):
            print("\t" + str(i + 1) + ") " + contacts_list[i])

        index_to_change = int(input("Which contact to remove? "))

        contact.remove_entry(contacts_list[index_to_change - 1])
    elif user_choise == 5:
        break