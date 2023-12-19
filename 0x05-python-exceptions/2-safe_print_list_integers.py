#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for a in range(x):
            if type(my_list[a]) is int:
                print("{:d}".format(my_list[a]), end="")
                count += 1
        print()
    except (IndexError):
        raise
    return count
