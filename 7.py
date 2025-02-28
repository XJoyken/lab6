import os

path = os.path.expanduser("~")
#existence
print(f"{path}:")
if os.path.exists(path):
    print("1. Exists")
else:
    print("1. Does not exist")

#readability
if os.access(path, os.R_OK):
    print("2. Readable")
else:
    print("2. Not readable")

#writability
if os.access(path, os.W_OK):
    print("3. Writable")
else:
    print("3. Not writable")

#executability
if os.access(path, os.X_OK):
    print("4. Executable")
else:
    print("4. Not executable")
