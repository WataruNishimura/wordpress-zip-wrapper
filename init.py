import glob

files = glob.glob("./test/**/*", recursive=True)

for file in files: 
  print(file)