O(1) - constant time
O(n) - linear, dependent on n. As the input doubles, so does the work (roughly).
O(n^2) - dependent on two O(n) within one another. Usually nested loops. For every item you process every other item.
O(log n) - task gradually shrinks each step as code runs
O(n log n) - You perform a logarithmic amount of work for each of the n elements

Enumerate() - allows for index and element to be accessed from list

List comprehension - more concise way to create new list using for loop within []

isalnum() - string method that returns true or false for a character being alphanumeric. True if it is a letter or digit.

Dictionary Solution is O(n) because you only need to loop once through both strings to build the dictionary and then checking if they are equal is also linear. That would make it O(n) + O(n) + O(n). For time complexity, you only look at highest order which would leave O(n).

