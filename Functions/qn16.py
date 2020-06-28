"""
16. Write a Python program to square and cube every number in a given list of
integers using Lambda.
"""


def square_num(num_list):
    square_nums = list(map(lambda x: x ** 2, num_list))
    print('Square of list:')
    print(square_nums)


def cube_num(num_list):
    print('\nCube of list:')
    cube_nums = list(map(lambda x: x ** 3, num_list))
    print(cube_nums)


num_list = [1, 2, 3, 4, 5]
square_num(num_list)
cube_num(num_list)
