"""
12. Write a Python script that takes input from the user and displays that input
back in upper and lower cases.

"""
def to_upper_lower(string):
    
    return string.lower(), string.upper()

input_str = input("Enter a string: ")
lower, upper = to_upper_lower(input_str)
print("Input String: "+input_str)
print("Lower case: "+lower)
print("Upper case: "+upper)