"""
3. Write a Python function to multiply all the numbers in a list.
"""


def mul_list(my_list):
    product = 1
    for x in my_list:
        product = product * x
    return product


my_list = [2, 3, 4]
print(mul_list(my_list))
