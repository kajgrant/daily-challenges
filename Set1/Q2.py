class Solution:
  def lengthOfLongestSubstring(self, s):
    
    max_substring = ''
    start = 0

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            substring = s[slice(start,i+1)]
            if len(substring) > len(max_substring):
                max_substring = substring
            start = i+1

    return len(max_substring)

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10