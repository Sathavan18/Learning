1) Base case in recusrion is the case that terminates the recursive call, without it, recursion will carry on until a Python's maximum recursion depth.

2) current.pop() undoes the choice we just made, restoring current to its previous state so we can explore another branch

4) Because each level has 2 possible outcomes, skip or take, there are 2^n subsets for n set.

5) Recursion solves a problem using smaller versions of the same problem. Backtracking uses recursion to explore multiple possible choices, then undoes a choice to explore another path.