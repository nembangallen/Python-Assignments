"""
 Write a Python program to get a string from a given string where all

occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t' 
"""


def replaced(input_string):
    substring = input_string[1:]
    for letter in range(1, len(substring)):
        if substring[letter] == input_string[0]:
            substring = substring.replace(substring[letter], '$')
    return input_string[0]+substring


print(replaced('anaconda'))
print(replaced('cyclic'))
print(replaced('nanotechnology'))
