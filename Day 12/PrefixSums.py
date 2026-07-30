# answer = prefix[right] - prefix[left - 1]
def build_prefix(nums):
    prefix = []
    for i in range(len(nums)):
        if i == 0:
            prefix.append(nums[i]) 
        else:
            prefix.append(nums[i]+ prefix[i-1]) 
    return prefix
def range_sum(prefix, left, right):
    if left == 0:
        answer = prefix[right]
    else:
        answer = prefix[right] - prefix[left - 1]
    return answer
nums = [3, 7, 2, 5, 8]
left = 0
right = 4
prefix = build_prefix(nums)
answer = range_sum(prefix,left,right)
print(answer)
