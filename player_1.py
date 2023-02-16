class Player:
    def __init__(self):
        self.used_words = []

    def count_words(self):
        return len(self.used_words)

    def add_word(self, word):
        self.used_words.append(word)

    def has_uses(self, word):
        return word in self.used_words

    def __repr__(self):
        return f' список {self.name_user} {self.used_words}'
