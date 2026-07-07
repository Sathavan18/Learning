# Creating:
# [new_value for item in collection]
# Filtering:
# [item for item in collection if condition]
'''
# Exercise 1:
numbers = [1,2,3,4]
double = [number * 2 for number in numbers]
print(double)

# Exercise 2
names = ["alice","bob","charlie"]
upper = [name.capitalize() for name in names]
print(upper)

# Exerise 3
numbers = [1,2,3,4,5,6]
even = [number for number in numbers if number%2 == 0]
print(even)

# Exercise 4
numbers = [1,2,3,4]
squares = []
for number in numbers:
    squares.append(number**2)
print(squares)
'''
# Exercise 5
# A list comprehension is a concise way of creating a new list 
# from an existing iterable, optionally transforming or 
# filtering the values.