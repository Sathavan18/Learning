# PART 1
# LIFO - last in first out

# append() - push onto a stack - O(1)
# pop() - pop from stack - O(1)
# [-1] - peak on top of stack - O(1)

# Part 3
'''
def remove_duplicates(s):
    track_stack = []
    for character in s:
        if track_stack == []:
            track_stack.append(character)
        elif track_stack[-1] == character:
            track_stack.pop()
        else:
            track_stack.append(character)
    return ''.join(track_stack)

s = "abbaca"
print(remove_duplicates(s))
'''