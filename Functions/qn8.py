"""
8. Write a Python function that takes a list and returns a new list with unique
elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""


def unique_list(my_list):
    unique_list = []

    for x in my_list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


print(unique_list([1, 2, 3, 3, 3, 4, 5, 5]))
