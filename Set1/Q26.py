def witnesses(heights):
    tallest = float('-inf')
    numWintess = 0

    for i in range(len(heights)-1, -1, -1):
        if heights[i] > tallest:
            tallest = heights[i]
            numWintess += 1

    return numWintess


print witnesses([3, 6, 3, 4, 1])
# 3

print witnesses([3, 4, 4, 4, 1])
# 2