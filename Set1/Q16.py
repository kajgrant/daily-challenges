def distance(s1, s2):
    return diff(s1, s2, l1=len(s1), l2=len(s2))


def  diff(s1, s2, l1, l2):

    if l1 == 0:
        return l2
 
    if l2 == 0:
        return l1
 

    if s1[l1-1] == s2[l2-1]:
        return diff(s1, s2, l1-1, l2-1)
 
    return 1 + min(diff(s1, s2, l1, l2-1),    # Insert
                   diff(s1, s2, l1-1, l2),    # Remove
                   diff(s1, s2, l1-1, l2-1)    # Replace
                   )

         
print distance('biting', 'sitting')
# 2