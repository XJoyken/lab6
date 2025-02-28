list = list(input().split())
with open("file2.txt", "w") as file:
    file.writelines("\n".join(list))