class Solution:
    def buddyStrings(self, A, B):
        noMatchA = []
        noMatchB = []
        j = 0

        for i in range(len(A)):
            if A[i] != B[i]:
                noMatchA.append(A[i])
                noMatchB.append(B[i])
                j+=1

        if len(noMatchA) > 2:
            return False
        elif (noMatchA[1] == noMatchB[0]) and (noMatchA[0] == noMatchB[1]):
            return True



print Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb')
# True
print Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb')
# False