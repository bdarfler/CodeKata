require 'test/unit'
require 'KataSix'


class KataSixTest < Test::Unit::TestCase
  @@anagram_dict = AnagramDictionary.new('/usr/share/dict/words')

  def test_canonical_representation
    assert_equal 'ehllo', AnagramDictionary.canonical_representation('hello')
  end

  def test_find_anagrams
    assert_equal %w(tablet battel).sort, @@anagram_dict.anagrams('battle').sort
  end

  def test_find_longest_anagrams
    assert_equal [%w(pneumohydropericardium hydropneumopericardium).sort,
                  %w(cholecystoduodenostomy duodenocholecystostomy).sort].sort,
                 @@anagram_dict.longest_anagrams().map { |x| x.sort }.sort
  end

  def test_find_most_anagrams
    assert_equal [%w(spale slape lapse saple salep elaps pales speal sepal lepas).sort,
                  %w(nagor rogan organ groan ronga orang argon goran angor grano).sort].sort,
                 @@anagram_dict.most_anagrams().map { |x| x.sort }.sort
  end

end