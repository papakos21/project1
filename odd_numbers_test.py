from odd_numbers import all_odd

def test_odd_numbers_1():
    assert all_odd(1) == [1]

def test_odd_numbers_2():
    assert all_odd(2) == [1]


def test_odd_numbers_3():
    assert all_odd(3) == [1, 3]


def test_odd_numbers_10():
    assert all_odd(10) == [1, 3, 5, 7, 9]