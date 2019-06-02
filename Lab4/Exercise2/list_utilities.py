class ListUtilities(list):

    def sift(self, n):
        sifted_list = []

        for word in self:
            if len(word) > n:
                sifted_list.append(word)

        return sifted_list