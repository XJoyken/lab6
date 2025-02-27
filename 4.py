import time
import math

def invoke_square():
    number = int(input())
    msc = int(input())
    time.sleep(msc / 1000)
    print(f"Square root of {number} after {msc} miliseconds is {math.sqrt(number)}")
invoke_square()