#!/usr/bin/python3


class MyList(list):
    def print_sorted(self):
        print(sorted(self))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
