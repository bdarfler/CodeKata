class KataFour

  def self.smallest_temp_spread(file_path='weather.dat', regex=/\s+(\d+)\D+(\d+)\D+(\d+)/)
    minimum = 9999999999
    result = nil
    File.foreach(file_path) do |line|
      if match = regex.match(line)
        one, two, three = match.captures
        spread = (two.to_i - three.to_i).abs
        if spread < minimum
          minimum = spread
          result = one
        end
      end
    end
    result
  end


  def self.smallest_score_spread(file_path='football.dat', regex=/\s+\d+\.\s+([a-zA-Z_]+)(?:\D+\d+){4}\D+(\d+)\D+(\d+)/)
    minimum = 9999999999
    result = nil
    File.foreach(file_path) do |line|
      if match = regex.match(line)
        one, two, three = match.captures
        spread = (two.to_i - three.to_i).abs
        if spread < minimum
          minimum = spread
          result = one
        end
      end
    end
    result
  end


  def self.smallest(file_path, regex)
    minimum = 9999999999
    result = nil
    File.foreach(file_path) do |line|
      if match = regex.match(line)
        one, two, three = match.captures
        spread = (two.to_i - three.to_i).abs
        if spread < minimum
          minimum = spread
          result = one
        end
      end
    end
    result
  end


  def self.smallest_temp_refactor
    smallest(file_path='weather.dat', pattern=/\s+(\d+)\D+(\d+)\D+(\d+)/)
  end

  def self.smallest_score_refactor
    smallest(file_path='football.dat', pattern=/\s+\d+\.\s+([a-zA-Z_]+)(?:\D+\d+){4}\D+(\d+)\D+(\d+)/)
  end
end