"""
8. Write a Python program to remove the nth index character 
from a nonempty string.
"""
def remove_character(input_string, n):
    first = input_string[:n]
    last = input_string[n+1:]
    return first + last

input_string = input('Enter a string: ')
print('Enter index upto :'+str(len(input_string)-1))
input_index = int(input())
print(remove_character(input_string,input_index))
print('Hello',2)