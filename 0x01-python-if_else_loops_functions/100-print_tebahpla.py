#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    i = (i, i - 32)[i % 2]
    print("{:c}".format(i), end="")
