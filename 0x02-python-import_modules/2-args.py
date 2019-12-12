#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nbarg = len(sys.argv) - 1
    print("{:d} argument".format(nbarg)+(":", ".")[nbarg == 0])
    for i in range(1, nbarg + 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
