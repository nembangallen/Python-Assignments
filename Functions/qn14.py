"""
14. Write a Python program to sort a list of dictionaries using Lambda.
"""


def sort_dict(laptops):
    print('Original list of laptops')
    print(laptops)
    sorted_laptops = sorted(laptops, key=lambda x: x['brand'])
    print('\nSorted:')
    print(sorted_laptops)


laptops = [{'brand': 'Dell', 'model': 'Inspiron 5555', 'color': 'Black'},
           {'brand': 'HP', 'model': 'Pavillion', 'color': 'Silver'},
           {'brand': 'Acer', 'model': 'Aspire', 'color': 'Blue'},
           {'brand': 'Apple', 'model': 'MBP', 'color': 'Silver'}]

sort_dict(laptops)
