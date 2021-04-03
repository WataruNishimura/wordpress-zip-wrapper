import pathlib
import argparse
import re
import os
import zipfile

# CLI: for parse args
parser = argparse.ArgumentParser(description="sample description")
#parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('target', help='Target folder')
parser.add_argument('output', help='Output file name and path')
parser.add_argument('-e','--exclude', help='Exclude target from the given file.', default='.zipexclude')
args = parser.parse_args()

exclude_file_path = pathlib.Path(args.exclude)
exclude_file_path = exclude_file_path.relative_to('')
exclude_file_flag = False

target_folder_path = pathlib.Path(args.target)
target_folder_path = target_folder_path.relative_to('')
target_folder_flag = False

output_file_path = pathlib.Path(args.output)
output_file_path = output_file_path .relative_to('')
output_file_flag = False

if(exclude_file_path.exists()):
  print("Exclude file exists")
  exclude_file_flag = True
else:
  print('\033[31m' + "ERROR : Exclude file does not exist" + '\033[0m')

if(target_folder_path.exists()):
  print("Target folder exists")
  os.chdir(target_folder_path)
  target_folder_flag = True
else:
  print('\033[31m' + "ERROR : Target folder does not exist"  + '\033[0m')

if(not output_file_path.exists()):
  print("Output file does not exist")
  output_file_flag = True
else:
  print('\033[31m' + "ERROR : Output file already exists"  + '\033[0m')



def filter(org_file):
  #return filter_flag
  return False

if __name__=='__main__': 
  if(exclude_file_flag == True and target_folder_flag == True and output_file_flag == True):
    pathlib_files = list(target_folder_path.glob("**/*"))
    target_files = list(target_folder_path.glob("**/*"))
    
    for file in pathlib_files:
      if(filter(file)):
        target_files.remove(file)

    for file_new in target_files:
      print(file_new)

    with zipfile.ZipFile(output_file_path, 'w') as new_zip: 
      for file in target_files:
        new_zip.write(file)
