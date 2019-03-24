def create(input_str):
    contacts_info = input_str.split(",")

    contacts_dict = {"name": " ", "address": " ", "birthday": " ", "phone number": " ", "email": " ", "profession": " ", "interests": " "}
    for contact in contacts_info:
        try:
            dict_key = contact.split(':')[0].strip().lower()
            dict_value = contact.split(':')[1].strip().lower()
        except:
            print("Not a valid format")

        if dict_key in contacts_dict:
            contacts_dict[dict_key] = dict_value
        else:
            print("Not a valid format")

    with open("contacts.txt", mode='a', encoding='utf-8') as file:
        string_to_write = ""
        for key, value in contacts_dict.items():
            string_to_write += key + ":" + value + ","

        file.write(string_to_write.strip(',') + "\n")


def search(input_str):
    try:
        parameter = input_str.split(':')[0].strip()
        value = input_str.split(':')[1].strip()
    except:
        print("Not a valid format")

    contacts_list = []

    if parameter == "name" or parameter == "address" or parameter == "birthday" or parameter == "phone number" or parameter == "email" or parameter == "profession" or parameter == "interests":
        with open("contacts.txt", mode='r', encoding='utf-8') as file:
            current_line = ' '
            while current_line != '':
                current_line = file.readline()

                if parameter + ":" + value in current_line:
                    contacts_list.append(current_line)
    else:
        print("Not a valid parameter")

    return contacts_list


def change_entry(searched_str, str_to_change):

    with open("contacts.txt", "r") as file:
        lines = file.readlines()
    with open("contacts.txt", "w") as file:
        for line in lines:
            if line.strip("\n") == searched_str.strip("\n"):
                file.write(str_to_change)
            else:
                file.write(line)


def remove_entry(str_to_remove):

    with open("contacts.txt", "r") as file:
        lines = file.readlines()
    with open("contacts.txt", "w") as file:
        for line in lines:
            if line.strip("\n") != str_to_remove.strip("\n"):
                file.write(line)