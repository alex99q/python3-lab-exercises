def number_of_occurrences(input_str):
    letters = []
    number_of_occurrences_list = []

    for letter in input_str:
        if letter not in letters:
            letters.append(letter)
            number_of_occurrences_list.append(1)
        else:
            index_of_current_letter = letters.index(letter)
            number_of_occurrences_list[index_of_current_letter] += 1

    for letter in letters:
        index_of_current_letter = letters.index(letter)
        occurrences = str(number_of_occurrences_list[index_of_current_letter])

        end_symbol = ""
        if index_of_current_letter != len(letters) - 1:
            end_symbol = ", "
        else:
            end_symbol = "\n"

        print("'" + letter + "'" + ":" + occurrences, end=end_symbol)