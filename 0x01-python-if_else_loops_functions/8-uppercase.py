#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if 96 < ord(s) < 123:
            s = chr(ord(s) - 32)
        print("{}".format(s), end='')
    print()

    #a function that prints a string in uppercase followed by a new line
    #def uppercase(str)
