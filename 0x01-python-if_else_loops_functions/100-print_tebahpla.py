#!/usr/bin/python3
for a in range(ord('z'), ord('a') - 1, -1):
    if a % 2 != 0:
        uppercase = ord('A') + (a - ord('a'))
        print("{:c}".format(uppercase), end="")
    else:
        print("{}".format(chr(a)), end="")
