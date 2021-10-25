# Contains some simple unsafe code examples to test code security analysis
import re

def match_url(url: str, regex=re.compile('(www|beta).example.com/')):
  """ Returns true if the url matches the regex """
  return regex.match(url)