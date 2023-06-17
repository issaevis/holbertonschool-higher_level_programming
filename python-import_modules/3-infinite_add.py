#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    i = 1
    if len(sys.argv) > 1:
        while i < len(sys.argv):
            sum += int(sys.argv[i])
            i += 1

    print("{}".format(sum))
