"""
2. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string.
Sample String : 'Python'
Expected Result : 'Pyon'
Sample String : 'Py'
Expected Result : 'PyPy'
Sample String : ' w'
Expected Result : Empty String
"""


def get_string(input_string):
    result = 'Empty String'
    if len(input_string) >= 2:
        result = input_string[0]+input_string[1] + \
            input_string[-2]+input_string[-1]
        return result
    else:
        return result


print(get_string('Python'))
print(get_string('Py'))
print(get_string('w'))
