import os
# file = open("opit.txt", "x")
path = os.path.expanduser(r"C:\Learning code\pp2\repositories\q2\lab6\opit.txt")
if os.path.exists(path):
    os.remove(path)
    print("file deleted")
else:
    print(f"path: {path} | does not exist")