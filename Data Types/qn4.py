"""
4. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""


def get_swaped(str1, str2):
    swaped = str1.replace(str1[0], str2[0]).replace(str1[1], str2[1]) + " " + \
        str2.replace(str2[0], str1[0]).replace(str2[1], str1[1])
    return swaped


print(get_swaped('abc', 'xyz'))
print(get_swaped('baunty', 'babli'))
print(get_swaped('ram', 'sam'))
