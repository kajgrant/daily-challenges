def products(nums):
  
  sumArr = []

  for num in nums:
    currSum = 1
    for i in nums:
      if num != i:
        currSum = currSum*i
    sumArr.append(currSum)

  return sumArr

print products([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]