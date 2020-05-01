from largest import find_largest


def test_find_largest_with_1():
    assert find_largest([-3, 4, 0]) == 4


def test_find_largest_with_2():
    assert find_largest([-3]) == -3


def test_find_largest_with_none():
    assert find_largest([]) is None
