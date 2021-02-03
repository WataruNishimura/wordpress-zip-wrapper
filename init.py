import pathlib

path = pathlib.Path("test")
pathlib_files = path.glob("**/*")

for file in list(pathlib_files):
  print(file)