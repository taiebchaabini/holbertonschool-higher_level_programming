#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    cond = lambda x:replace if x == search else x
    for i in range(len(my_list)):
        new_list.append(cond(my_list[i]))
    return (new_list)
