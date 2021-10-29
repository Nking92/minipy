from unsafe import *
import tarfile
import os
import shutil

def test_match_url():
  assert(match_url('www.example.com/'))
  assert(match_url('beta.example.com/'))
  assert(not match_url('www33example.com/'))
  # Demonstrate vulnerability - this shouldn't work
  assert(match_url('www3example.com/'))

def make_tarfile(output_filename, source_dir):
  # From https://stackoverflow.com/a/17081026
  with tarfile.open(output_filename, "w:gz") as tar:
      tar.add(source_dir, arcname=os.path.basename(source_dir))

def test_extract_from_zip():
  tmp_dir = os.path.join(os.getcwd(), 'tmp')
  example_dir = os.path.join(tmp_dir, 'example')
  sub_dir = os.path.join(example_dir, '1')
  tar_filename = os.path.join(tmp_dir, 'tmp.tar.gz')
  unzip_dir = os.path.join(tmp_dir, 'tmp_unzip')
  os.makedirs(sub_dir, exist_ok=True)
  make_tarfile(tar_filename, example_dir)
  extract_from_zip(tar_filename, unzip_dir)
  unzip_example_dir = os.path.join(unzip_dir, 'example')
  unzip_sub_dir = os.path.join(unzip_example_dir, '1')
  unzip_example_dir_exists = os.path.exists(unzip_example_dir)
  unzip_sub_dir_exists = os.path.exists(unzip_sub_dir)
  shutil.rmtree(tmp_dir)
  assert(unzip_example_dir_exists)
  assert(unzip_sub_dir_exists)

def test_extract_from_zip_safely():
  # This only runs a basic test. It doesn't check for TarSlip.
  tmp_dir = os.path.join(os.getcwd(), 'tmp')
  example_dir = os.path.join(tmp_dir, 'example')
  sub_dir = os.path.join(example_dir, '1')
  tar_filename = os.path.join(tmp_dir, 'tmp.tar.gz')
  unzip_dir = os.path.join(tmp_dir, 'tmp_unzip')
  os.makedirs(sub_dir, exist_ok=True)
  make_tarfile(tar_filename, example_dir)
  extract_from_zip_safely(tar_filename, unzip_dir)
  unzip_example_dir = os.path.join(unzip_dir, 'example')
  unzip_sub_dir = os.path.join(unzip_example_dir, '1')
  unzip_example_dir_exists = os.path.exists(unzip_example_dir)
  unzip_sub_dir_exists = os.path.exists(unzip_sub_dir)
  shutil.rmtree(tmp_dir)
  assert(unzip_example_dir_exists)
  assert(unzip_sub_dir_exists)