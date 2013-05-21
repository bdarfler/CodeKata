require 'digest/sha2'

class BloomFilter
  def initialize(filename=nil, step=3)
    @step = step
    @bit_array = Array.new(2 ** (8 * step), false)
    File.foreach(filename) { |word| insert(word.strip) } unless filename.nil?
  end

  def hashes(string)
    hash_val = Digest::SHA512.digest(string.downcase)
    pattern = "H#{@step * 2}" * (hash_val.size / @step)
    hash_val.unpack(pattern).map { |x| x.hex }
  end

  def insert(string)
    hashes(string).each { |hash_val| @bit_array[hash_val] = true }
  end

  def contains(string)
    hashes(string).inject(true) { |acc, hash_val| acc && @bit_array[hash_val] }
  end
end