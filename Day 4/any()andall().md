any():
any() returns True if at least one element in an iterable is truthy. Otherwise, it returns False.
essentially it means at least one truthy element. 
0, "", and False are considered False.
use list comprehension for any()
example:
numbers = [2, 4, 6, 8, 9]
# is there an odd number?
return(any(number%2==0 for number in numbers))
# returns true as there is 9

all():
all() returns True if every element (or every condition) is True. Otherwise, it returns False.
example:
numbers = [2, 4, 6, 8, 9]
# are they all odd number?
all(number % 2 != 0 for number in numbers)
# returns False as not all of them are True