def char_count(input_str):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    char_count_dict = {"vowels": 0, "consonants": 0, "digits": 0, "whitespaces": 0}

    for c in input_str:
        if c in vowels:
            char_count_dict["vowels"] += 1
        elif c in consonants:
            char_count_dict["consonants"] += 1
        elif c in digits:
            char_count_dict["digits"] += 1
        elif c == " ":
            char_count_dict["whitespaces"] += 1

    return char_count_dict