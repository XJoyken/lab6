string = input("")
string2 = "".join(reversed(string))
if string2 == string:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
