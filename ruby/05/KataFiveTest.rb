require 'test/unit'
require 'KataFive'

class KataFiveTest < Test::Unit::TestCase
  @@spell_checker = BloomFilter.new('/usr/share/dict/words')

  def test_contains
    word = 'hello'
    bloom_filter = BloomFilter.new()
    bloom_filter.insert(word)
    assert(bloom_filter.contains(word), "filter should contain #{word}")
  end

  def test_does_not_contain
    word = 'hello'
    bloom_filter = BloomFilter.new()
    bloom_filter.insert("#{word} world")
    assert(!bloom_filter.contains(word), "filter should not contain #{word}")
  end

  def test_spelling_contains
    word = 'hello'
    assert(@@spell_checker.contains(word), "#{word} should be a word")
  end

  def test_spelling_does_not_contain
    word = 'bobloblaw'
    assert(!@@spell_checker.contains(word), "#{word} should not be a word")
  end
end
