import os

def extract(path):
    all_files_dirs = os.listdir(path)
    directories = [i for i in all_files_dirs if os.path.isdir(os.path.join(path, i))]
    files = [i for i in all_files_dirs if os.path.isfile(os.path.join(path, i))]
    all = [i for i in all_files_dirs]
    print(f"Directories in {path}:", directories)
    print(f"Files in {path}: ", files)
    print(f"All directories and files in {path}:", all)

path = os.path.expanduser("~")
extract(path)