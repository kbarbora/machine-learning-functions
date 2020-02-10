#!/usr/bin/python3
# """
# Functions to obtain dataset from URL or specified path
# pp44
# @author Kevin Barba
# """

import os
import tarfile
import wget

def fetch_data_url(url, filename, dest_path):
  if not os.path.isdir(dest_path):
    os.makedirs(dest_path)
  file_path = os.path.join(url, filename)
  downloaded = wget.download(file_path, out=dest_path)
  tar = tarfile.open(downloaded)
  tar.extractall(path=dest_path)
  tar.close()
  return

def main():
  url = "https://github.com/ageron/handson-ml/raw/master/datasets/housing"
  filename = "housing.tgz"

  fetch_data_url(url, filename, "./data")

if __name__ == '__main__':
  main()

  
