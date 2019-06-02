from string_utilities import StringUtilities

sentence = StringUtilities(input("Type your sentence: "))

print("The longest word is " + str(sentence.longest_word()) + " characters long")