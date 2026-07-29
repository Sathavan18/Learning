'''
numbers = [2, 4, 6, 8, 10]
left = 0
right = len(numbers) - 1
# while left < right: -> compares indexes

def is_palindrome(word):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True
word1 = 'racecar'
print(is_palindrome(word1))

def add_up(numbers,target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return (numbers[left],numbers[right])
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1
    return None
numbers = [1, 2, 4, 6, 8, 11]
target = 10
print(add_up(numbers,target))
'''
#LeetCode 125 — Valid Palindrome with Two Pointers

def isPalindrome(s):
    s = s.lower()
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left].isalnum() == False:
            left += 1
        elif s[right].isalnum() == False:
            right -= 1
        else:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
    return True
    
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))