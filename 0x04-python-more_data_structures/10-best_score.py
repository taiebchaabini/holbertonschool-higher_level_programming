#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None):
        return None
    key = list(a_dictionary.values())[0]
    #key = -99999999999999999999
    res = ""
    c = 0
    for i, v in a_dictionary.items():
        if (v >= key):
            key = v
            res = i
            c += 1
    if (c == len(list(a_dictionary.values()))):
        return None
    return res
