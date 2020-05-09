from list_of_three import get_word


def test_get_word_with_abcdefghi():
    assert get_word('abcdefghi') == [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]


def test_get_word_with_many_characters():
    assert get_word("lalalalalallsldld") == "too long!!!!"


def test_get_word_with_less_characters():
    assert get_word("karolos") == [['k', 'a', 'r'], ['o', 'l', 'o'], ['s', ' ', ' ']]
