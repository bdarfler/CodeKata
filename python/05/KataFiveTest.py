import unittest
from KataFive import BloomFilter


class Test(unittest.TestCase):
    spell_checker = BloomFilter('/usr/share/dict/words')

    def test_contains(self):
        bloom_filter = BloomFilter()
        bloom_filter.insert("hello")
        self.assertTrue(bloom_filter.contains("hello"), 'filter should contain "hello"')

    def test_does_not_contains(self):
        bloom_filter = BloomFilter()
        bloom_filter.insert("world")
        self.assertFalse(bloom_filter.contains("hello"), 'filter should not contain "hello"')

    def test_spell_checker_contains(self):
        self.assertTrue(self.spell_checker.contains("hello"), '"hello" should be a word')

    def test_spell_checker_does_not_contain(self):
        word = 'bobloblaw'
        self.assertFalse(self.spell_checker.contains(word), '"' + word + '" should not be a word')


if __name__ == "__main__":
    unittest.main()
