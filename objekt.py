class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subword = subwords

    def checking_words(self, input_user):
        if input_user in self.subword:
            return True
        return False

    def len_subword(self):
        return len(self.subword)

    def __repr__(self):
        return f'{self.word} содержит  {len(self.subword)} слов'
