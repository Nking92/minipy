# Contains some simple unsafe code examples to test code security analysis
import re
import tarfile

def match_url(url: str, regex=re.compile('(www|beta).example.com/')):
  """ Returns true if the url matches the regex """
  return regex.match(url) is not None

def extract_from_zip(zip_name, dest_path):
  """ Extracts a tar or zip file into a folder """
  # example from https://github.com/github/codeql/blob/main/python/ql/src/Security/CWE-022/examples/tarslip_bad.py
  with tarfile.open(zip_name) as tar:
      # BAD - relative paths in tar entry can access any file on the filesystem
      for entry in tar:
          tar.extract(entry, dest_path)

def extract_from_zip_safely(zip_name, dest_path):
  """
  Safely extracts a tar or zip file into a folder. 
  Avoids the TarSlip vulnerability by validating paths inside the zip file.
  """
  import os
  # example from https://github.com/github/codeql/blob/main/python/ql/src/Security/CWE-022/examples/tarslip_good.py
  with tarfile.open(zip_name) as tar:
    for entry in tar:
        #GOOD: Check that entry is safe
        if os.path.isabs(entry.name) or ".." in entry.name:
            raise ValueError("Illegal tar archive entry")
        tar.extract(entry, dest_path)