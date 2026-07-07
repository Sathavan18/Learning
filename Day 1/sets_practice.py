'''
# SETS DON'T CONTAIN DUPLICATES
# add() adds an element to a set assuming not duplicate, else remains same
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

# remove() removes an element from the set
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

# intersection() returns set containing intersection of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# union() returns set with all items in both sets without duplicates (as normal in sets)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)
'''