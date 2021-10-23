# Contains some simple unsafe code examples to test code security analysis
import re

def match_url(url: str, regex=re.compile('(www|beta).example.com/')):
  return regex.match(url)