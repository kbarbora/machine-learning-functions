#!/usr/bin/python3
# """
# Functions to obtain dataset from URL or specified path
# pp44
# @author Kevin Barba
# """

import os
import tarfile
import wget
import numpy as np
import sklearn

def fetch_data_url(url, filename, dest_path):
  if not os.path.isdir(dest_path):
    os.makedirs(dest_path)
  file_path = os.path.join(url, filename)
  downloaded = wget.download(file_path, out=dest_path)
  tar = tarfile.open(downloaded)
  tar.extractall(path=dest_path)
  tar.close()
  return

def split_train_test(data: 'panda.Dataframe', test_ratio: 'int') -> 'tuple':
  """
  Split train and test data from a pandas dataframe with the indicated test data ratio
  """
  shuffle_indices = np.random.permutation(len(data))
  test_set_size = int(len(data) * test_ratio)
  test_indices = shuffled_indices[:test_set_size]
  train_indices = shuffled_indices[test_set_size:]
  return data.iloc[train_indices], data.iloc[test_indices]

def


def main():
  url = "https://github.com/ageron/handson-ml/raw/master/datasets/housing"
  filename = "housing.tgz"

  fetch_data_url(url, filename, "./data")

if __name__ == '__main__':
  main()

  
