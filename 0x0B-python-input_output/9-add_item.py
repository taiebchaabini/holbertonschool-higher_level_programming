#!/usr/bin/python3
"""
   a script that adds all arguments to a Python list, and then
   save them to a file:
"""
import sys
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

filename = "add_item.json"
current_list = []

try:
    current_list = load_from_json_file(filename)
    args = sys.argv[1:]
    for i in args:
        current_list.append(i)
except FileNotFoundError:
    pass
finally:
    save_to_json_file(current_list, filename)
