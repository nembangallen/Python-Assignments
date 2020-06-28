"""
3. Write a Python program to get a string from a given string where all

occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t' 
"""


def get_output(input_string):

    first_char = input_string[0]  # Assign first character of input string
    i = 1
    result_string = first_char

    while i < len(input_string):
        if input_string[i] != first_char:
            result_string += input_string[i]
        else:
            result_string += '$'
        i += 1
    return result_string


print(get_output('restart'))
print(get_output('anaconda'))
print(get_output('cyclic'))
