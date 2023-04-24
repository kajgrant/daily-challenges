class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


def largestNum(nums):
  largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
  return '0' if largest_num[0] == '0' else largest_num

  

print largestNum([17, 7, 2, 45, 72])
# 77245217