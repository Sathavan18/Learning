What is recursion?
Recursion is a technique where a function solves a problem by calling itself on a smaller version of the same problem until it reaches a base case.

Why is a base case necessary?
So that the recursion can stop.

What would happen if a recursive function didn't have a base case?
Recursion will continue forever (before RecursionError)

When we call a recursive function, where is each function call stored?
The call stack

What's the difference between:
factorial(5)
calling
factorial(4)
and a for loop? I'm asking about how the computer executes them.
A for loop is sequential, whereas factorial(5) will wait for factorial(4) to execute, waiting on a stack.

Suppose I write:
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
Without running it,what is printed?
Say it started with countdown(5), then it would be 5,4,3,2,1

Now change it to:
def countdown(n):
    if n == 0:
        return
    countdown(n - 1)
    print(n)
What gets printed now?
Say it started with countdown(5), then it would be 1,2,3,4,5

What's the space complexity of recursion usually based on?
The maximum recursion depth (the call stack).
For example, factorial(5) has five stack frames, so O(n).

Time Complexity
How many total function calls are made?

Space Complexity
How many function calls exist at the same time?