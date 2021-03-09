import pathlib
import argparse

# CLI: for parse args
parser = argparse.ArgumentParser(description="sample description")
#parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('input', help='Set target folder')
parser.add_argument('output', help='Set output zip file name')
parser.add_argument('-e','--exclude', help='Exclude target from the given file.', default='.zipexclude')
args = parser.parse_args()

exclude_file_path = pathlib.Path(args.exclude)
exclude_file_flag = False

if(exclude_file_path.exists()):
  print("Exclude file exists")
  exclude_file_flag = True

# Get file and folder list in specific directories.
path = pathlib.Path(args.input)
pathlib_files = path.glob("**/*")

for file in list(pathlib_files):
  print(file)

