require 'test/unit'
require 'KataFour'


class KataFourTest < Test::Unit::TestCase
    def test_weather
        assert_equal('14', KataFour.smallest_temp_spread())
    end
    
    def test_football
        assert_equal('Aston_Villa', KataFour.smallest_score_spread())
    end
    
    def test_weather_refactor
        assert_equal('14', KataFour.smallest_temp_refactor())
    end
    
    def test_football_refactor
        assert_equal('Aston_Villa', KataFour.smallest_score_refactor())
    end                                                                           
end
