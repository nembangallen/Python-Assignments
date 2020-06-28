"""
1. Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com' Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""
from collections import Counter

eg_str = "google.com"

char_freq = Counter(eg_str)
print(str(char_freq))