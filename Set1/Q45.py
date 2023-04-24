class Solution:
  def reverseWords(self, str):
    wordArr = str.split(" ")

    newStr = ""

    for word in wordArr:
        size = len(word)
        newWord = ""
        for i in range(len(word)-1, -1, -1):
            print word[i]
            newWord += word[i]    
        newStr += newWord + " "

    return newStr[:-1]



print Solution().reverseWords("The cat in the hat")
# ehT tac ni eht tah