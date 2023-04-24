def jumpToEnd(nums):
    num_size = len(nums)

    if num_size == 1: return 0

    reachableIndex = 0
    previousReachableIndex = 0
    jump = 0

    for curr in range(num_size):
        if curr + nums[curr] >= reachableIndex:
            reachableIndex = curr + nums[curr]

        if curr == previousReachableIndex:
            jump += 1
            previousReachableIndex = reachableIndex
            if previousReachableIndex >= num_size -1:
                return jump


print jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4])
# 2