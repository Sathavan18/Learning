# enumerate() lets me loop over both the index and the value together.
# use enumerate() when you need the indes AND the value
# Example:
'''
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(index, name)
print(enumerate(names))

# Exercise 1:
fruits = ["Apple", "Banana", "Orange"]
for index, name in enumerate(fruits):
    print(index,name)

# Exercise 2:
fruits = ["Apple", "Banana", "Orange"]
for index, name in enumerate(fruits):
    print(index+1,name)

# Exercise 3:
numbers = [10, 15, 20, 25, 30]
for index,name in enumerate(numbers):
    if index % 2 == 0:
        print(name)

# Exercise 4
names = ["Alice", "Bob", "Charlie", "David"]
for index,name in enumerate(names):
    if name == 'Charlie':
        print(index)

# Exercise 5
for index,name in enumerate(names):
    print(index,name)
'''
# Question	Answer
#What problem does it solve?	Gives both index and value while looping.
#What does it return?	An enumerate object (producing index/value pairs).
#When should I use it?	When I need the index and the value.
#When should I NOT use it?	When I only need the values.
#Common interview use	Finding positions, numbering output, tracking indexes.
#Common beginner mistake	Confusing the index with the value (like Exercise 3).
