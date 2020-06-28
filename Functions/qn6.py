"""
6. Write a Python function to check whether a number is in a given range.
"""


def check_range(n):
    if n in range(1, 10):
        print(" %s is in the range." % str(n))
    else:
        print(" %s is not in the range." % str(n))


check_range(7)
