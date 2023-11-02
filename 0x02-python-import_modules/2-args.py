#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    len1 = len(sys.argv) - 1
    if len1 == 0:
        print("0 arguments.")
    elif len1 == 1:
        print("{} argument:".format(len1))
    else:
        print("{} arguments:".format(len1))
    for i in range(len1):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
