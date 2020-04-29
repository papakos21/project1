from odd_numbers import all_odd


def test_odd_numbers_2():
    assert all_odd(2) == [1]


def test_odd_numbers_3():
    assert all_odd(3) == [1, 3]


def test_odd_numbers_10():
    assert all_odd(10) == [1, 3, 5, 7, 9]

# all_odd(2) returns [1]
# all_odd(3) returns [1,3]

# all_odd(10) returns [1,3,5,7,9]
