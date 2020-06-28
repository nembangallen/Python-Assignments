num1 = [2, 3, 4, 5, 7, 10]
num2 = [1, 2, 5, 6, 7, 12]
print('Initial arrays: ')
print(num1)
print(num2)
result = list(filter(lambda x: x in num1, num2))
print('\n Intersection: ')
print(result)
