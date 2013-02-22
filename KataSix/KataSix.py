class AnagramDictionary(object):
    def __init__(self, filename):
        self.underlying = {}
        self.longest_length = 0
        self.longest_canonical = set()
        self.most_length = 0
        self.most_canonical = set()
        with open(filename) as f:
            for word in f:
                self.insert(word.strip())

    @staticmethod
    def canonical_representation(string):
        return ''.join(sorted(string.lower()))

    def insert(self, string):
        canonical = self.canonical_representation(string)
        anagrams = self.underlying.get(canonical, set())
        anagrams.add(string.lower())
        self.underlying[canonical] = anagrams
        self.update_stats(canonical, anagrams)

    def update_stats(self, canonical, anagrams):
        if len(anagrams) > 1:
            if len(canonical) == self.longest_length:
                self.longest_canonical.add(canonical)
            elif len(canonical) > self.longest_length:
                self.longest_length = len(canonical)
                self.longest_canonical = {canonical}
            if len(anagrams) == self.most_length:
                self.most_canonical.add(canonical)
            elif len(anagrams) > self.most_length:
                self.most_length = len(anagrams)
                self.most_canonical = {canonical}

    def get_anagrams(self, string):
        canonical = self.canonical_representation(string)
        anagrams = self.underlying.get(canonical, set())
        return anagrams - {string.lower()}

    def get_longest_anagrams(self):
        return [self.underlying.get(canonical) for canonical in self.longest_canonical]

    def get_most_anagrams(self):
        return [self.underlying.get(canonical) for canonical in self.most_canonical]