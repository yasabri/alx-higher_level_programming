#!/usr/bin/python3i
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return ("None")
    else:
        return my_list[idx]
