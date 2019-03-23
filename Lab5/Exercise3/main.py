from morse_code import encrypt_to_morse

user_input = input("Type in here: ")

file_input = ""
with open("input.txt", mode='r', encoding='utf-8') as f:
    file_input = f.read()

#try:
#    f = open("input.txt", mode='r', encoding='utf-8')
#    file_input = f.read()
#finally:
#    f.close()

print("Morse from input: " + encrypt_to_morse(user_input))
print("Morse from file: " + encrypt_to_morse(file_input))