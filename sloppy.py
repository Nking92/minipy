# Code snippets that might be considered bad style

def concatenate_strings(s1, s2, s3, s4, s5, s6, s7, s8, s9):
    """ Concatenates the strings and returns the result """
    return s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9

def concatenate_strings_with_default(p1, p2, p3, p4, p5, p6, p7, p8, p9=r'foo'):
    """ Concatenates the strings and returns the result """
    return p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9

def say_hello(name=r'Sam'):
    """ Returns a string "Hello <name>" with the name filled in """
    return f"Hello {name}"