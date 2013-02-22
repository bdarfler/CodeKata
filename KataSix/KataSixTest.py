import unittest
from KataSix import AnagramDictionary


class Test(unittest.TestCase):
    anagram_dict = AnagramDictionary('/usr/share/dict/words')

    def test_canonical_representation(self):
        self.assertEqual(AnagramDictionary.canonical_representation("hello"), "ehllo")

    def test_find_anagrams(self):
        self.assertEqual(self.anagram_dict.get_anagrams('battle'), {"tablet", "battel"})

    def test_find_longest_anagrams(self):
        print(self.anagram_dict.get_longest_anagrams())

    def test_find_most_anagrams(self):
        print(self.anagram_dict.get_most_anagrams())


if __name__ == "__main__":
    unittest.main()
