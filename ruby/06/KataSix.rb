require 'set'

class AnagramDictionary
  def initialize(filename)
    @underlying = Hash.new
    @longest_length = 0
    @longest_canonical = Set.new
    @most_length = 0
    @most_canonical = Set.new
    File.foreach(filename) { |word| insert(word.strip) }
  end

  def self.canonical_representation(string)
    string.downcase.chars.sort.join
  end

  def insert(string)
    canonical = self.class.canonical_representation(string)
    anagrams = @underlying[canonical] ||= Set.new
    anagrams.add(string.downcase)
    @underlying[canonical] = anagrams
    update_stats(canonical, anagrams)
  end

  def update_stats(canonical, anagrams)
    if anagrams.size > 1
      if canonical.size == @longest_length
        @longest_canonical.add(canonical)
      elsif canonical.size > @longest_length
        @longest_length = canonical.size
        @longest_canonical = Set.new(canonical)
      end
      if anagrams.size == @most_length
        @most_canonical.add(canonical)
      elsif anagrams.size > @most_length
        @most_length = anagrams.size
        @most_canonical = Set.new(canonical)
      end
    end
  end

  def get_anagrams(string)
    canonical = self.class.canonical_representation(string)
    anagrams = @underlying[canonical] ||= Set.new
    anagrams.delete(string.downcase)
  end

  def get_longest_anagrams
    @longest_canonical.map { |canonical| @underlying[canonical] }
  end

  def get_most_anagrams
    @most_canonical.map { |canonical| @underlying[canonical] }
  end
end
