def chop( value, array ):
    return next((pos for pos, item in enumerate(array) if item == value), -1)

if __name__ == '__main__':
    assert -1 is chop(3, [])
    assert -1 is chop(3, [1])
    assert 0 is chop(1, [1])
    #
    assert 0 is chop(1, [1, 3, 5])
    assert 1 is chop(3, [1, 3, 5])
    assert 2 is chop(5, [1, 3, 5])
    assert -1 is chop(0, [1, 3, 5])
    assert -1 is chop(2, [1, 3, 5])
    assert -1 is chop(4, [1, 3, 5])
    assert -1 is chop(6, [1, 3, 5])
    #
    assert 0 is chop(1, [1, 3, 5, 7])
    assert 1 is chop(3, [1, 3, 5, 7])
    assert 2 is chop(5, [1, 3, 5, 7])
    assert 3 is chop(7, [1, 3, 5, 7])
    assert -1 is chop(0, [1, 3, 5, 7])
    assert -1 is chop(2, [1, 3, 5, 7])
    assert -1 is chop(4, [1, 3, 5, 7])
    assert -1 is chop(6, [1, 3, 5, 7])
    assert -1 is chop(8, [1, 3, 5, 7])