import os

def check(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"Filename of {path}:", filename)
        print(f"Directory of {path}:", directory)
    else:
        print(f"Path: {path} | does not exist")
path = os.path.expanduser("~")
check(path)