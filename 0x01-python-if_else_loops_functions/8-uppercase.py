#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) >= ord('a') and ord(a) <= ord('z'):
            a = chr(ord('A') + (ord(a) - ord('a')))
        print("{}".format(a), end="")
    print()
