import unittest
from KataSix import AnagramDictionary


class Test(unittest.TestCase):
    anagram_dict = AnagramDictionary('/usr/share/dict/words')

    def test_canonical_representation(self):
        self.assertEqual(AnagramDictionary.canonical_representation("hello"), "ehllo")

    def test_find_anagrams(self):
        self.assertEqual(self.anagram_dict.get_anagrams('battle'), {"tablet", "battel"})

    def test_find_longest_anagrams(self):
        self.assertEqual(self.anagram_dict.get_longest_anagrams(),
                         [{'pneumohydropericardium', 'hydropneumopericardium'},
                          {'cholecystoduodenostomy', 'duodenocholecystostomy'}])

    def test_find_most_anagrams(self):
        self.assertEqual(self.anagram_dict.get_most_anagrams(),
                         [{'spale', 'slape', 'lapse', 'saple', 'salep', 'elaps', 'pales', 'speal', 'sepal', 'lepas'},
                          {'nagor', 'rogan', 'organ', 'groan', 'ronga', 'orang', 'argon', 'goran', 'angor', 'grano'}])


if __name__ == "__main__":
    unittest.main()
