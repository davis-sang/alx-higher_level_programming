#!/usr/bin/python3
def roman_to_int(roman_string):
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) != str or roman_string is None:
        return 0
    sum = 0
    i = 0
    for c in roman_string:
        sum += num[c] if num[c] <= i else num[c] - i * 2
        i = num[c]
    return sum
