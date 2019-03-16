user_input = input("Sentence to count the vowels: ").lower()

vowel_number_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for current_letter in user_input:
    if current_letter in vowel_number_dict:
        vowel_number_dict[current_letter] += 1

print(vowel_number_dict)