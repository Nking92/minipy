from sloppy import *

def test_concatenate_strings():
    result = concatenate_strings('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
    assert(result == 'abcdefghi')

def test_concatenate_strings_with_default():
    result = concatenate_strings_with_default('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    assert(result == 'abcdefghfoo')

def test_say_hello():
    result = say_hello("Sam")
    assert(result == 'Hello Sam')