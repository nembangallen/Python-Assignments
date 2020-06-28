"""
1. Write a Python function to find the Max of three numbers.
"""


def find_max(x, y, z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z


print(find_max(6, -10, 4))
print(find_max(9, 18, 20))
