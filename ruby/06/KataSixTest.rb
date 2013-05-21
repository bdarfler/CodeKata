require 'test/unit'
require 'KataSix'


class KataSixTest < Test::Unit::TestCase
  @@anagram_dict = AnagramDictionary.new('/usr/share/dict/words')

  def test_canonical_representation
    assert_equal(AnagramDictionary.canonical_representation('hello'), 'ehllo')
  end

  def test_find_anagrams
    assert_equal(%w(tablet battel).to_set, @@anagram_dict.get_anagrams('battle'))
  end

  def test_find_longest_anagrams
    assert_equal([%w(pneumohydropericardium hydropneumopericardium).to_set,
                  %w(cholecystoduodenostomy duodenocholecystostomy).to_set],
                 @@anagram_dict.get_longest_anagrams())
  end

  def test_find_most_anagrams
    assert_equal([%w(nagor rogan organ groan ronga orang argon goran angor grano).to_set,
                  %w(spale slape lapse saple salep elaps pales speal sepal lepas).to_set],
                 @@anagram_dict.get_most_anagrams())
  end

end