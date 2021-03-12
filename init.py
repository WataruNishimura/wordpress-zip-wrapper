import pathlib
import argparse
import re
import os

# CLI: for parse args
parser = argparse.ArgumentParser(description="sample description")
#parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('target', help='Set target folder')
parser.add_argument('output', help='Set output zip file name')
parser.add_argument('-e','--exclude', help='Exclude target from the given file.', default='.zipexclude')
args = parser.parse_args()

exclude_file_path = pathlib.Path(args.exclude)
exclude_file_flag = False

# Get file and folder list in specific directories.
target_folder = pathlib.Path(args.target)
pathlib_files = target_folder.glob("**/*")

target_files = pathlib_files

def filter(org_file):
  #return filter_flag
  return 0

if(exclude_file_path.exists()):
  print("Exclude file exists")
  exclude_file_flag = True
else:
  print('\033[31m' + "ERROR : Exclude file does not exist" + '\033[0m')

if(target_folder.exists()):
  print("Target folder exists")
  exclude_file_flag = True
else:
  print('\033[31m' + "ERROR : Target folder does not exist"  + '\033[0m')


if __name__=='__main__': 
  for file in list(pathlib_files):
    if(filter(file)):
      target_files.remove(file)
  
  for file in list(target_files):
    print(file)