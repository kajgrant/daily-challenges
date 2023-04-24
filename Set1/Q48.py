def getBonuses(performance):

    size = len(performance)
    bonusArr = []

    for i in range(size):
        bonus = 1
        if i == 0:
            extra = performance[i] - performance[i+1]
            if extra < 0: extra = 0
            else: extra = 1
            bonusArr.append(bonus + extra)
        elif i == size-1:
            extra = performance[i] - performance[i-1]
            if extra < 0: extra = 0
            else: extra = 1
            bonusArr.append(bonus + extra)
        else:
            extraL = performance[i] - performance[i+1]
            extraR = performance[i] - performance[i-1]
            if extraL < 0: extraL = 0 
            else: extraL = 1
            if extraR < 0: extraR = 0
            else: extraR = 1
            bonusArr.append(bonus + extraL + extraR)

    return bonusArr


print getBonuses([1, 2, 3, 2, 3, 5, 1])
# [1, 2, 3, 1, 2, 3, 1]