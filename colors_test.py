import colors


def test_black_or_white_returns_white_for_0():
    assert colors.black_or_white(0) == 'white'


def test_black_or_white_returns_black_for_1():
    assert colors.black_or_white(1) == 'black'


def test_my_colors_returns_blue_for_1():
    assert colors.my_colors(1) == 'black'




def test_my_colors_returns_blue_for_2():
    assert colors.my_colors(2) == 'blue'

def test_my_colors_returns_unknown_for_all_the_rest():
    assert colors.my_colors(10) == 'unknown'

def test_my_colors_map_returns_blue_for_2():
    assert colors.my_colors_map(2) == 'blue'


def test_my_colors_map_returns_blue_for_1():
        assert colors.my_colors_map(1) == 'black'