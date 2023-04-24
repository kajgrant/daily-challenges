class Solution(object):
  def threeSum(self, nums):
    n = len(nums)
    arr = []

    found = False

    for i in range(0, n-2):
      for j in range(i+1, n-1):
        for k in range(j+1, n):
          if (nums[i] + nums[j] + nums[k] == 0):
            arr.append(nums[i])
            arr.append(nums[j])
            arr.append(nums[k])
            found = True

    if found == False:
      return None
    else:
      return arr


# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]