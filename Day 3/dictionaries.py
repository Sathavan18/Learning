'''
def isRepeated(text):
    check_repeated = dict()
    for character in text:
        if character in check_repeated:
            return character
        else:
            check_repeated[character] = 1
    return None

text = 'abca'
print(isRepeated(text))
'''
# TwoSum(Optimal):
def twoSum(nums,target):
    two_sum_pairs = dict()
    for i in range(len(nums)):
        if target - nums[i] in two_sum_pairs:
            return [two_sum_pairs[target-nums[i]],i]
        else:
            two_sum_pairs[nums[i]] = i

nums = [12,7,2,15]
target = 9
print(twoSum(nums,target))