from morse_code import encrypt_to_morse, morse_to_sound
import time

user_input = input("Type in here: ")

file_input = ""
with open("input.txt", mode='r', encoding='utf-8') as f:
    file_input = f.read()

#try:
#    f = open("input.txt", mode='r', encoding='utf-8')
#    file_input = f.read()
#finally:
#    f.close()

morse_from_input = encrypt_to_morse(user_input)
morse_from_file = encrypt_to_morse(file_input)

print("Morse from input: " + morse_from_input)
print("Morse from file: " + morse_from_file)

choise_for_sound = input("Do you want to hear the morse code (type in \"yes\" or \"no\")?: ")

if choise_for_sound == "yes":
    morse_to_sound(morse_from_input)
    time.sleep(1)
    morse_to_sound(morse_from_file)