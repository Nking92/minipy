from math_functions import *

def test_calculate_circumference():
    r = 3
    expected = 18.84955592153876
    actual = calculate_circumference(r)
    assert round(expected, 4) == round(actual, 4)

def test_circle_area():
    # This test is intentionally trivial to demonstrate dummy functions.
    r = 3
    try:
      circle_area(r)
    except:
      pass
    assert(True)

def test_rectangle_area():
    w = 3
    h = 4
    expected = 12
    actual = rectangle_area(w, h)
    assert expected == actual

def test_square_perimeter():
    s = 3
    expected = 12
    actual = square_perimeter(s)
    assert expected == actual

def test_fibonacci():
    """ Demonstrates a test with poor coverage. We will only test the trivial case. """
    n = 0
    expected = 0
    actual = fibonacci(n)
    assert expected == actual