#!/usr/bin/python3
def roman_to_int(roman_string):
    if(type(roman_string) != str or roman_string is None):
        return (0)
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    v = ""
    res = 0
    for i in range(len(roman_string)):
        v = roman_string[i]
        res += my_dict[v]
        if (i == 1 and roman_string[0] is "I" and strlen(roman_string) == 2):
            res = my_dict[v] - i
            print(roman_string[0])
    return (res)
