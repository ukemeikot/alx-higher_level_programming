#!/usr/bin/python3
def remove_char_at(str, n):
    new = []
    for a in range(0, len(str)):
        if a != n:
            new.append(str[a])
    return "".join(new)
