from largest import find_largest


def test_find_largest_with_4():
    assert find_largest([-3, 4, 0]) == 4


def test_find_largest_with_3():
    assert find_largest([-3]) == -3


def test_find_largest_with_none():
    assert find_largest([]) is None
