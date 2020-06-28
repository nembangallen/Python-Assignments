"""
12. Write a Python program to create a function that takes one argument, and
that argument will be multiplied with an unknown given number.
"""


def mul_num(n):
    return lambda x: x*n


product = mul_num(2)
print("Multiplied by 2: "+str(product(10)))
product = mul_num(4)
print("Multiplied by 4: "+str(product(10)))
