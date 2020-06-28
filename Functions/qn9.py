"""
9. Write a Python function that takes a number as a parameter and check the
number is prime or not.
"""


def check_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                print(str(n) + ' is not a prime number')
                break

        else:
            print(str(n)+' is a prime number')
    else:
        print(str(n)+' is not a prime number')


check_prime(7)
check_prime(-2)
check_prime(4)
