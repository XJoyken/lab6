string = input("")
lower_case = sum(map(str.islower, string))
upper_case = sum(map(str.isupper, string))
print(f"Lower: {lower_case}, Upper: {upper_case}")