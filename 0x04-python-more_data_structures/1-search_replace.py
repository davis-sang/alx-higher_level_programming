#!/usr/bin/python3
def search_replace(my_list, searh, replace):
    new_list = [replace if i == search else i for i in my_list]
    return (new_list)
