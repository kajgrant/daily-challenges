def permute(nums):
    ans_arr = []
    dfs(nums, [], ans_arr)
    return ans_arr
        

def dfs(nums, path, ans_arr):
    if not nums:
        ans_arr.append(path)
    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1], path+[nums[i]], ans_arr)

print(permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]