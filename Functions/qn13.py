"""
13. Write a Python program to sort a list of tuples using Lambda.
"""


def sort_tuple(total_student):
    print('Original List of tuples: ')
    print(total_student)
    total_student.sort(key=lambda x: x[1])
    print('\nSorted:')
    print(total_student)


total_student = [('Class I', 60), ('Class II', 53),
                 ('Class III', 70), ('Class V', 40)]
sort_tuple(total_student)
