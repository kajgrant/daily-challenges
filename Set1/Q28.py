def maximum_product_of_three(lst):
    min1 = lst[0]
    min2 = lst[1]
    max1 = lst[2]
    max2 = lst[3]

    for i in range(len(lst)):
        if lst[i] < min1 and lst[i] < min2:
            min2 = min1
            min1 = lst[i]
        elif lst[i] > min1 and lst[i] < min2:
            min2 = lst[i]

        if lst[i] > max1 and lst[i] > max2:
            max2 = max1
            max1 = lst[i]
        elif lst[i] < max1 and lst[i] > max2:
            max2 = lst[i]

    sum1 = min1*min2*max2
    sum2 = min2*max1*max1

    if sum1 > sum2:
        return sum1
    else:
        return sum2


print maximum_product_of_three([-4, -4, 2, 8, -1, 4])
# 128