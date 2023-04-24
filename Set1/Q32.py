def max_subarray_sum(arr):
    max_so_far = arr[0]
    max_ending_here = 0

    for i in range(len(arr)):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < 0:
            max_ending_here = 0

        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    
    return max_so_far

print max_subarray_sum([34, -50, 42, 14, -5, 86])
# 137