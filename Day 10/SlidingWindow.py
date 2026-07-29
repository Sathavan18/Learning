def max_sum_subarray(nums, k):
    total = 0
    #calculate first window
    for i in range(k):
        total += nums[i]

    max_total = total
    #slide the window
    for i in range(k, len(nums)):
        total = total - nums[i-k] + nums[i]
        if total > max_total:
            max_total = total
    
    return max_total