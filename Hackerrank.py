# Stacks
'''
def isValid(s):
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in s:
        if character == '(' or character == '{' or character == '[':
            stack.append(character)
        else:
            if stack == []:
                return False
            elif stack[-1] != pairs[character]:
                return False
            else:
                stack.pop()
    return stack == []

check = '([{()}])'
print(isValid(check))
'''
# Queue
