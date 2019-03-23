names = input("Your name is: ").split()

first_name_char = names[0][0]
middle_name_char = names[1][0]
last_name = names[2]

print("{}.{}.{}".format(first_name_char, middle_name_char, last_name))