#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
r = (number % 10) if number > 0 else (number * -1) % 10
# YOUR CODE HERE
if (r > 5 and number > 0):
    print(f"Last digit of {num} is {r} and is greater than 5")
elif (r == 0):
    print(f"Last digit of {num} is {r} and is 0")
elif (number < 0 or r < 6):
    if (number < 0):
        print(f"Last digit of {num} is -{r} and is less than 6 and not 0")
    else:
        print(f"Last digit of {num} is {r} and is less than 6 and not 0")
