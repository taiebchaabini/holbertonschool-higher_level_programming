#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None):
        return None
    key = list(a_dictionary.values())[0]
    res = ""
    for i, v in a_dictionary.items():
        if (v >= key):
            key = v
            res = i
    return res
