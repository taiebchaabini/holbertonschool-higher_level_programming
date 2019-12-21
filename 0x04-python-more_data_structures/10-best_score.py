#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None):
        return None
    key = -9999999
    res = ""
    for i, v in a_dictionary.items():
        if (v >= key):
            key = v
            res = i
    return res
