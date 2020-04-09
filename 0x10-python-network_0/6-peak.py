#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers.
"""
def find_peak(list_of_integers):
    try:
        my_list = list_of_integers
        if (len(my_list) == 0):
            return None;
        peak = []
        for i in range(len(my_list)):
            if my_list[i-1] < my_list[i] and my_list[i+1] <\
            my_list[i]:
                peak.append(my_list[i])
        if len(peak) == 0:
            peak = my_list[0]
        else:
            peak = peak[0]
    except Exception:
        peak = None;
    return peak;
