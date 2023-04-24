def buy_and_sell(arr):
    low = arr[0]
    max_diff = 0

    for i in range(len(arr)):
        low = min(low, arr[i])
        diff = arr[i] - low
        max_diff = max(max_diff, diff)

    return max_diff
  
print buy_and_sell([9, 11, 8, 5, 7, 10])
# 5