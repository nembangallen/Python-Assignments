# 15. Write a Python program to filter a list of integers using Lambda.

def filter_list(nums):
    print('Input List: ')
    print(nums)
    print('\nNumbers greater than 10:')
    result = list(filter(lambda x: x > 10, nums))
    print(result)


nums = [1, 3, 7, 8, 9, 10, 12, 13, 15, 17]
filter_list(nums)
