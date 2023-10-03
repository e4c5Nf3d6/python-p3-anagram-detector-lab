class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, l):
        matches = []
        for x in l:
            if sorted([*x.lower()]) == sorted([*self.word.lower()]):
                matches.append(x)
        return matches
