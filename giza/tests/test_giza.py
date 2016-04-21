from giza import calc_square

def test_calc_square():
    assert calc_square(2, verbosity=0) ==  4
    assert calc_square(4, verbosity=1) == 16
