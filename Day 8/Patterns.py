'''
def first_repeated(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return number
        else:
            seen.add(number)
    return False

numbers = [1,2,3,4,5]
print(first_repeated(numbers))
numbers2 = [1,2,3,2,5]
print(first_repeated(numbers2))
'''
# Given an integer list nums and an integer k, return True if 
# there are two equal values whose indices are at most k apart.
def contains_nearby_duplicate(nums, k):
    track = dict()
    for index,value in enumerate(nums):
        if value in track:
            if index - track[value] <= k:
                return True
        track[value] = index
    return False
nums = [1, 2, 3, 1]
k = 3
print(contains_nearby_duplicate(nums,k))