from unsafe import *

def test_match_url():
  assert(match_url('www.example.com/'))
  assert(match_url('beta.example.com/'))
  # Demonstrate vulnerability - this shouldn't work
  assert(match_url('www3example.com/'))