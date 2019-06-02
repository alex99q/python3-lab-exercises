class StringUtilities(str):

    def longest_word(self):
        word_list = self.split()

        longest_word_length = 0
        for word in word_list:
            word = StringUtilities.remove_symbols(word)

            if len(word) > longest_word_length:
                longest_word_length = len(word)

        return longest_word_length

    @staticmethod
    def remove_symbols(input_str):

        for char in input_str:
            if (ord(char) >= 32 and ord(char) <= 64 and not char.isdigit()) or (ord(char) >= 91 and ord(char) <= 96):
                 input_str = input_str.replace(char, "")

        return input_str