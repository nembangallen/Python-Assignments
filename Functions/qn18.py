"""
18. Write a Python program to check whether a given string is number or not
using Lambda.
"""

is_num = lambda x: x.replace('.','',1).isdigit()
print(is_num('6789898'))
print(is_num('adsdsds'))