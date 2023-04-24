def buy_and_sell(arr):

    if not arr or len(arr) == 1:
        return 0

    buy = arr[0]
    sell = arr[1]

    profit = sell - buy

    for i in range(1, len(arr)-1):

        if arr[i] < buy:

            for j in range(i+1, len(arr)):
                if (arr[j] - arr[i]) > profit: 
                    sell = arr[j]
                    buy = arr[i]

    profit = sell - buy
    return profit


print buy_and_sell([9, 11, 8, 5, 7, 10])
# 5

print buy_and_sell([9, 11, 5, 4, 3, 2])
# 2

print buy_and_sell([12, 11, 5, 4, 3, 2])
# -1