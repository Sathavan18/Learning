'''
def first_repeated(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return number
        else:
            seen.add(number)
    return False
numbers = [4, 2, 7, 1, 2, 7]
print(first_repeated(numbers))

class Solution(object):
    def middleNode(self,head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        return 'Invalid number'
'''