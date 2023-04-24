#You are given an array of integers. Return the length of the longest consecutive elements sequence in the array.
#For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive sequence 1, 2, 3, 4, and thus, you should return its length, 4.

def longest_consecutive(nums):

    if len(nums) == 0:
        return 0

    sortArr = sorted(nums)
    num_consec = 0

    for i in range(1,len(sortArr)-1,1):
        if sortArr[i-1]+1 == sortArr[i]:
            num_consec += 1

    if num_consec > 0:
        num_consec += 1

    return num_consec


print longest_consecutive([100, 4, 200, 1, 3, 2])
# 4