import pathlib
import argparse

# argparse init parser 
parser = argparse.ArgumentParser(description="sample description")
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
args = parser.parse_args()

print(args)

exclude_file_path = pathlib.Path(".zipexclude")
exclude_file_flag = False

if(exclude_file_path.exists()):
  print("Exclude file exists")
  exclude_file_flag = True

path = pathlib.Path("test")
pathlib_files = path.glob("**/*")

for file in list(pathlib_files):
  print(file)

