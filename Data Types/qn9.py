"""
9. Write a Python program to change a given string to a new string where the first
and last chars have been exchanged.
"""
def change_char(input_string):
    str_list = list(input_string)
    str_list[0], str_list[-1] = str_list[-1], str_list[0]
    return "".join(str_list)

input_string = input("Enter a string: ")
print(change_char(input_string))
print(change_char('Papichulo'))
