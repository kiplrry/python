#!/usr/bin/python3
def uppercase(st):
    for i in st:
        if ord('a') <= ord(str(i)) <= ord('z'):
            print("{}".format(chr(ord(str(i)) - 32)), end="")
        else:
            print("{}".format(i), end='')
    print("")
uppercase("best")
uppercase("Best School 98 Battery street")
