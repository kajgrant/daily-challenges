def jumpToEnd(nums):

    num_jumps = 0
    
    if not nums:
        return num_jumps

    i = 0
    while(i < len(nums)):
        biggest_jump = nums[i]

        for j in range(1, min(nums[i]+1, len(nums)-i)):
            if nums[i+j] > biggest_jump:
                biggest_jump = nums[i+j]

        i = i + biggest_jump
        num_jumps = num_jumps + 1
        if i >= len(nums):
            return num_jumps
    
    return num_jumps


print jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4])
# 2
