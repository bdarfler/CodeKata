require 'test/unit'
require 'KataTwo'

class KataTwoTest < Test::Unit::TestCase

    def test_chop_iterative
        assert_equal(-1, KataTwo.chop_iterative(3, []))
        assert_equal(-1, KataTwo.chop_iterative(3, [1]))
        assert_equal(0, KataTwo.chop_iterative(1, [1]))
        #
        assert_equal(0, KataTwo.chop_iterative(1, [1, 3, 5]))
        assert_equal(1, KataTwo.chop_iterative(3, [1, 3, 5]))
        assert_equal(2, KataTwo.chop_iterative(5, [1, 3, 5]))
        assert_equal(-1, KataTwo.chop_iterative(0, [1, 3, 5]))
        assert_equal(-1, KataTwo.chop_iterative(2, [1, 3, 5]))
        assert_equal(-1, KataTwo.chop_iterative(4, [1, 3, 5]))
        assert_equal(-1, KataTwo.chop_iterative(6, [1, 3, 5]))
        #
        assert_equal(0, KataTwo.chop_iterative(1, [1, 3, 5, 7]))
        assert_equal(1, KataTwo.chop_iterative(3, [1, 3, 5, 7]))
        assert_equal(2, KataTwo.chop_iterative(5, [1, 3, 5, 7]))
        assert_equal(3, KataTwo.chop_iterative(7, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.chop_iterative(0, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.chop_iterative(2, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.chop_iterative(4, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.chop_iterative(6, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.chop_iterative(8, [1, 3, 5, 7]))
    end

    def test_chop_recursive
        assert_equal(-1, KataTwo.chop_recursive(3, []))
        assert_equal(-1, KataTwo.chop_recursive(3, [1]))
        assert_equal(0, KataTwo.chop_recursive(1, [1]))
        #
        assert_equal(0, KataTwo.chop_recursive(1, [1, 3, 5]))
        assert_equal(1, KataTwo.chop_recursive(3, [1, 3, 5]))
        assert_equal(2, KataTwo.chop_recursive(5, [1, 3, 5]))
        assert_equal(-1, KataTwo.chop_recursive(0, [1, 3, 5]))
        assert_equal(-1, KataTwo.chop_recursive(2, [1, 3, 5]))
        assert_equal(-1, KataTwo.chop_recursive(4, [1, 3, 5]))
        assert_equal(-1, KataTwo.chop_recursive(6, [1, 3, 5]))
        #
        assert_equal(0, KataTwo.chop_recursive(1, [1, 3, 5, 7]))
        assert_equal(1, KataTwo.chop_recursive(3, [1, 3, 5, 7]))
        assert_equal(2, KataTwo.chop_recursive(5, [1, 3, 5, 7]))
        assert_equal(3, KataTwo.chop_recursive(7, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.chop_recursive(0, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.chop_recursive(2, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.chop_recursive(4, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.chop_recursive(6, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.chop_recursive(8, [1, 3, 5, 7]))
    end
    
    def test_chop_slice_recursive
        assert_equal(-1, KataTwo.slice_recursive(3, []))
        assert_equal(-1, KataTwo.slice_recursive(3, [1]))
        assert_equal(0, KataTwo.slice_recursive(1, [1]))
        #
        assert_equal(0, KataTwo.slice_recursive(1, [1, 3, 5]))
        assert_equal(1, KataTwo.slice_recursive(3, [1, 3, 5]))
        assert_equal(2, KataTwo.slice_recursive(5, [1, 3, 5]))
        assert_equal(-1, KataTwo.slice_recursive(0, [1, 3, 5]))
        assert_equal(-1, KataTwo.slice_recursive(2, [1, 3, 5]))
        assert_equal(-1, KataTwo.slice_recursive(4, [1, 3, 5]))
        assert_equal(-1, KataTwo.slice_recursive(6, [1, 3, 5]))
        #
        assert_equal(0, KataTwo.slice_recursive(1, [1, 3, 5, 7]))
        assert_equal(1, KataTwo.slice_recursive(3, [1, 3, 5, 7]))
        assert_equal(2, KataTwo.slice_recursive(5, [1, 3, 5, 7]))
        assert_equal(3, KataTwo.slice_recursive(7, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.slice_recursive(0, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.slice_recursive(2, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.slice_recursive(4, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.slice_recursive(6, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.slice_recursive(8, [1, 3, 5, 7]))
    end
    
    def test_chop_slice_iterative
        assert_equal(-1, KataTwo.slice_iterative(3, []))
        assert_equal(-1, KataTwo.slice_iterative(3, [1]))
        assert_equal(0, KataTwo.slice_iterative(1, [1]))
        #
        assert_equal(0, KataTwo.slice_iterative(1, [1, 3, 5]))
        assert_equal(1, KataTwo.slice_iterative(3, [1, 3, 5]))
        assert_equal(2, KataTwo.slice_iterative(5, [1, 3, 5]))
        assert_equal(-1, KataTwo.slice_iterative(0, [1, 3, 5]))
        assert_equal(-1, KataTwo.slice_iterative(2, [1, 3, 5]))
        assert_equal(-1, KataTwo.slice_iterative(4, [1, 3, 5]))
        assert_equal(-1, KataTwo.slice_iterative(6, [1, 3, 5]))
        #
        assert_equal(0, KataTwo.slice_iterative(1, [1, 3, 5, 7]))
        assert_equal(1, KataTwo.slice_iterative(3, [1, 3, 5, 7]))
        assert_equal(2, KataTwo.slice_iterative(5, [1, 3, 5, 7]))
        assert_equal(3, KataTwo.slice_iterative(7, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.slice_iterative(0, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.slice_iterative(2, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.slice_iterative(4, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.slice_iterative(6, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.slice_iterative(8, [1, 3, 5, 7]))
    end
    
    def test_chop
        assert_equal(-1, KataTwo.chop(3, []))
        assert_equal(-1, KataTwo.chop(3, [1]))
        assert_equal(0, KataTwo.chop(1, [1]))
        #
        assert_equal(0, KataTwo.chop(1, [1, 3, 5]))
        assert_equal(1, KataTwo.chop(3, [1, 3, 5]))
        assert_equal(2, KataTwo.chop(5, [1, 3, 5]))
        assert_equal(-1, KataTwo.chop(0, [1, 3, 5]))
        assert_equal(-1, KataTwo.chop(2, [1, 3, 5]))
        assert_equal(-1, KataTwo.chop(4, [1, 3, 5]))
        assert_equal(-1, KataTwo.chop(6, [1, 3, 5]))
        #
        assert_equal(0, KataTwo.chop(1, [1, 3, 5, 7]))
        assert_equal(1, KataTwo.chop(3, [1, 3, 5, 7]))
        assert_equal(2, KataTwo.chop(5, [1, 3, 5, 7]))
        assert_equal(3, KataTwo.chop(7, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.chop(0, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.chop(2, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.chop(4, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.chop(6, [1, 3, 5, 7]))
        assert_equal(-1, KataTwo.chop(8, [1, 3, 5, 7]))
    end
end