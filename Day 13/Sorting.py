def find_unique_pairs(nums, target):
    nums.sort()
    pairs = []

    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            pairs.append((nums[left],nums[right]))
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
        
    return pairs

# Bubble Sort
def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        swapped = False

        for j in range(n-1-i):
            if nums[j] > nums[j + 1]:
                # swap
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                swapped = True

        if not swapped:
            break

    return nums

# Selection Sort
def selection_sort(nums):
    n = len(nums)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums

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