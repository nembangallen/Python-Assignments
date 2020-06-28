"""
10. Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""


def get_even(my_list):
    even_list = []
    for item in my_list:
        if (item % 2 == 0):
            even_list.append(item)
        else:
            pass
    return even_list


print(get_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
