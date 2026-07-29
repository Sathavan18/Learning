A recursive function has a base case which stops the recursion.
Methods call themselves, calls are formed into a stack. LIFO. 
When there is a return, it ends the method on that particular function call.
A recursive function doesn't keep reusing one execution. Every recursive call creates a brand-new function call with its own local variables, and each call waits on the call stack until the function it called finishes.

e.g.
def test(n):
    if n == 0:
        print("Base")
        return

    print("Down", n)
    test(n - 1)
    print("Up", n)

test(2)

Output:
Down 2
Down 1
Base
Up 1
Up 2

Code before the recursive call executes on the way down.
Code after the recursive call executes on the way back up.

e.g. 
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

factorial(4)
↓
factorial(3)
↓
factorial(2)
↓
factorial(1)