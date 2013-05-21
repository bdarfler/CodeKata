class AnagramDictionary
  def initialize(filename)
    @underlying = {}
    @longest_length = 0
    @longest_canonical = {}
    @most_length = 0
    @most_canonical = {}
    File.foreach(filename) { |word| insert(word.strip) }
  end

  def self.canonical_representation(string)
    string.downcase.chars.sort.join
  end

  def insert(string)
    canonical = self.class.canonical_representation(string)
    anagrams = @underlying[canonical] ||= {}
    anagrams[string.downcase] = nil
    @underlying[canonical] = anagrams
    update_stats(canonical, anagrams)
  end

  def update_stats(canonical, anagrams)
    if anagrams.size > 1
      if canonical.size == @longest_length
        @longest_canonical[canonical] = nil
      elsif canonical.size > @longest_length
        @longest_length = canonical.size
        @longest_canonical = {canonical => nil}
      end
      if anagrams.size == @most_length
        @most_canonical[canonical] = nil
      elsif anagrams.size > @most_length
        @most_length = anagrams.size
        @most_canonical = {canonical => nil}
      end
    end
  end

  def anagrams(string)
    canonical = self.class.canonical_representation(string)
    anagrams = @underlying[canonical] ||= {}
    anagrams.reject { |k, v| k == string.downcase }.keys
  end

  def longest_anagrams
    @longest_canonical.keys.map { |x| @underlying[x].keys }
  end

  def most_anagrams
    @most_canonical.keys.map { |x| @underlying[x].keys }
  end
end
