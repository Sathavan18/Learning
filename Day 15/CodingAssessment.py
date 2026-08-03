'''
# Binary Search
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return - 1
nums = [1,2,3,4,5,6]
target = 6
print(binary_search(nums,target))
# Time Complexity = O(logn) - search half of the array after each run
# Space Complexity = O(1)

# Prefix Sums
def build_prefix(nums):
    prefixes = [nums[0]]
    for i in range(1, len(nums)):
        prefixes.append(nums[i] + prefixes[i-1])
    return prefixes
def range_sum(prefix, left, right):
    if left == 0:
        answer = prefix[right]
    else:
        answer = prefix[right] - prefix[left - 1]
    return answer

nums = [3, 7, 2, 5, 8]
prefix = build_prefix(nums)
print(prefix)
print(range_sum(prefix, 1, 3))

# Bubble Sort
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range (n-1-i): # after sort, last i elements sorted and don't need to be compared again
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                swapped = True
        if not swapped:
            break
    return nums
# Time Complexity: O(n^2)
# Best Time With swapped: O(n)
# Space Complexity: O(1)            

# Selection Sort
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n): # after first swap, first element guaranteed smallest, so skip it
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]    
    return nums
# Time Complexity: O(n^2)
# Best Time: O(n^2)
# Space Complexity: O(1)

# Insertion Sort
def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        position = i - 1

        while position >= 0 and nums[position] > key:
            nums[position + 1] = nums[position]
            position -= 1
        nums[position + 1] = key
    return nums
# Time Complexity: O(n^2)
# Best Time: O(n^2)
# Space Complexity: O(1)
'''
# Sliding Window - Leetcode 643
def findMaxAverage(nums, k):
    total = 0
    for i in range(k):
        total += nums[i]
    average = total/float(k)
    for i in range(k,len(nums)):
        total = (total - nums[i-k] + nums[i])
        if (total/float(k)) > average:
            average = total/float(k)
    return average
