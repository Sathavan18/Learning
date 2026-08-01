'''
# Lower Bound
def lower_bound(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left
nums = [1, 2, 2, 2, 4, 5]
target = 2
print(lower_bound(nums,target))

# Upper Bound
def upper_bound(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left
nums = [1, 2, 2, 2, 4, 5]
target = 2
print(upper_bound(nums,target))
'''