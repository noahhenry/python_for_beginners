from pathlib import Path


# Absolute path
  # Starts at the root of our hard disc
  # i.e. Windows -> c:\Program Files\Microsoft
  # i.e. Mac -> /usr/local/bin

# Relative path
  # Starts relative to the current file path

path = Path("notes")
print(path.exists())

# make a path if it does not exist
path2 = Path("emails")
print(path2.mkdir())
path2.rmdir() # delete directory

# how about opening and reviewing a files data?
path3 = Path()
for file in path3.glob("*"): # in glob(), we define a search pattern
  print(file)