#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for c in range(x):
        try:
            print("{:d}".format(my_list[c]), end="")
        except (TypeError, ValueError):
            c -= 1
            pass
    print("")
    return (c)
