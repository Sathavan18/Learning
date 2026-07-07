'''
# append() adds an item to the end of the list
a = [1,2,3,4,5]
a.append(6)
print(a)

# pop() removes the last item of the list
a = [1,2,3,4,5]
a.pop()
print(a)

# insert() adds an item in a specific position
a = [1,2,3,4,5]
a.insert(1,1) #index,value
print(a)

# remove() removes an item specified
a = [1,2,3,4,5]
a.remove(2)
print(a)

# sort() sorts a list in order, works for strings also
a = [2,3,4,1,5,6]
a.sort()
print(a)
b = ['a','c','f','b','d']
b.sort()
print(b)

# sorted() returns sorted list, can specify ascending or descending
a = [2,3,4,1,5,6]
print(sorted(a))
b = [2,3,4,1,5,6]
print(sorted(b,reverse=True))

# reverse() returns reversed list
a = [2,3,4,1,5,6]
a.reverse()
print(a) #can't do a.reverse() here as it returns None

# extend() adds specified list at the end of current list
a = [2,3,4,1,5,6]
b = [7,8,9]
a.extend(b)
print(a)
'''