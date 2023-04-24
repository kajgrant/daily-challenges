def check(lst):
    num_modify = 0

    for i in range(len(lst)-1):
        if  lst[i] > lst[i+1]:
            num_modify += 1

    if num_modify <= 1:
        return True
    else:
        return False

print check([13, 4, 7])
# True
print check([5,1,3,2,5])
# False