"""
7. Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters.

Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""


def calculate(str):
    d = {'upper_case': 0, "lower_case": 0}
    for letter in str:
        if letter.isupper():
            d['upper_case'] += 1
        elif letter.islower():
            d['lower_case'] += 1
        else:
            pass
    print("No. of Upper case characters: ", d['upper_case'])
    print("No. of Lower case characters: ", d['lower_case'])


calculate('The quick Brown Fox jump over the Lazy Dog')
