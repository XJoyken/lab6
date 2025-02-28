# import os #for deleting
# os.remove("copy.txt")
with open("original.txt", "r") as first:
    with open("copy.txt", "w") as second:
        second.writelines(first)