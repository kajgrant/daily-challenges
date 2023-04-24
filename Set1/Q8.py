def two_sum(list, k):
  
    for i in range(len(list)):
        for j in range(len(list)):
            if (list[i] + list[j] == k) and (i != j):
                return True
    
    return False


print two_sum([4,7,1,-3,2], 5)
# True