"""
10. Write a Python program to remove the characters which have odd index
values of a given string.
"""
def remove_odd(string):
    output = ''
    for i in range(len(string)):
        if i % 2 == 0:
            output = output + string[i]
    return output

string = input("Enter string: ")
print(remove_odd(string))
print(remove_odd('Zigzag'))