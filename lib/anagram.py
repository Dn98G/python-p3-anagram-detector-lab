class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    def match(self,word_list):
        sorted_word = sorted(self.word)
        matches = []

        for word in word_list:
            if sorted_word == sorted(word.lower()) and word.lower() != self.word:
                matches.append(word)
        return matches
        