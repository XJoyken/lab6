list = list(map(int, input().split()))
result = 1
for i in range(len(list)):
    result *= list[i]
print(result)
