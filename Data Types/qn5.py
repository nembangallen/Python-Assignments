"""
5. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged.

Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""


def add_suffix(input_string):
    if len(input_string) >= 3:
        check_ing = input_string[-3:]
        if check_ing == 'ing':
            input_string = input_string + 'ly'
        else:
            input_string = input_string + 'ing'
    return input_string


print(add_suffix('abc'))
print(add_suffix('string'))
print(add_suffix('xd'))
