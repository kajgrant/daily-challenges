def singleNumber(nums):
  
    initial = nums[0]

    for i in range(1,len(nums)):
        initial = initial ^ nums[i]

    return initial
  
print singleNumber([4, 3, 7, 2, 6, 4, 1, 3, 2, 6, 7])
# 1