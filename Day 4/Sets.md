Creating a set:
1) 
Create a set contatining apple,banana,orange
fruits = {'apple','banana','orange'}

2) 
Difference between a={} and a = set()
a = {} creates an empty dictionary, a = set() creates an empty set

3) 
It will contain apple, banana, orange. There aren't duplicates in sets so the second apple won't be there.

Set Methods:
1) add()
fruits = {"apple", "banana"}
fruits.add("orange")
This will add orange to the set. IT modifies the original set. When printed, it will have orange in the set. Don't know specific interview scenario.

2) remove()
fruits.remove("banana")
This will remove banana from the set. It modifies the original set. When printed, it will no longer have banana in the set. Don't know specific interview scenario.

3) discard()
similar to remove but won't raise an error if the item is not in the set unlike remove. It does modify the original set. In an interview, they may ask in the question don;t have errors raised which will make me need to use discard over remove.

4) intersection()
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.intersection(B))
this will print 3 and 4 as they are commonalities in both sets. intersection selects the common items in sets, returning a new set and prints them.

5) union()
A = {1, 2}
B = {2, 3}
print(A.union(B))
this will print 1,2,3. union combines two sets together without duplicates, returning a new set.

6) difference()
A = {1, 2, 3, 4}
B = {3, 4}
print(A.difference(B))
this will print 1,2. difference() only wants the non common elements. direction matters for this method, so it's everything in A not in B.

Exercises:
1) Remove Duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
no_duplicates_numbers = set(numbers)
print(no_duplicates_numbers)

2) Common Elements
A = [1, 2, 3, 4]
B = [3, 4, 5, 6]
print(A.intersection(B)) X Need to convert to sets first

3) Elements Only in A
A = [1, 2, 3, 4]
B = [3, 4]
print(A.difference(B))  X Need to convert to sets first

4) Do They Share Anything?
A = [1, 2, 3]
B = [5, 6, 3]
C = A.intersection(B)  X Need to convert to sets first
if len(C) > 0: return True
return False

5) First Duplicate
numbers = [7, 2, 5, 2, 9, 7]
seen = set()
for number in numbers:
    if number in seen:
        return number
    else:
        seen.add(number)

6) Count Unique Words
sentence_list = sentence.split()
sentence_set = set(sentence_list)
return len(sentence_set)