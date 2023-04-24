def count_invalid_parenthesis(string):
    leftCount = 0
    rightCount = 0

    for char in string:
        if char == '(':
            leftCount += 1
        if char == ')':
            rightCount += 1

    return abs(leftCount-rightCount)
    

print count_invalid_parenthesis("()())()")
# 1         