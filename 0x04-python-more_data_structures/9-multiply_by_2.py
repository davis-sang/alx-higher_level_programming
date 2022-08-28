#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    t = {}
    for k in a_dictionary:
        t[k] = a_dictionary[k] * 2
    return(t)
