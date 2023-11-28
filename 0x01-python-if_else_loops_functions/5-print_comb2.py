#!/usr/bin/python3
for a in range(0, 100):
    if a == 99:
        print(f"{a:02d}")
    else:
        print("{:02d}".format(a), end=", ")
