#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("0 arguments.")

elif len(sys.argv) == 1:
    print("1 argument:\n{}".format(sys.argv[1]))
else:
    print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(len(sys.argv)):
        if i > 0:
            print("{}: {}".format(i, sys.argv[i]))
