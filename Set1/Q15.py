def findPythagoreanTriplets(nums):
    s = len(nums)
    j = 0

    for i in range(s - 2):
        for k in range(j + 1, s):
            for j in range(i + 1, s - 1):
                # Calculate square of array elements
                x = nums[i]*nums[i]
                y = nums[j]*nums[j]
                z = nums[k]*nums[k]
                if (x == y + z or y == x + z or z == x + y):
                    return True
     
    # If we reach here, no triplet found
    return False
    
        

print findPythagoreanTriplets([3, 12, 5, 13])
# True