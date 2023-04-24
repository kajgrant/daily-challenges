class Solution(object):
  def compress(self, chars):
    
    arr_size = len(chars)
    compress_arr = []
    compress_val = 1

    if arr_size == 0:
        return None
    
    compress_arr.append(chars[0])

    for i in range(1,arr_size):
        if chars[i] == chars[i-1]:
            compress_val += 1
        else:
            if compress_val > 1:
                compress_arr.append(compress_val) 
            compress_val = 1
            compress_arr.append(chars[i])

    if compress_val > 1:  
        compress_arr.append(compress_val)

    return compress_arr




print Solution().compress(['a', 'a', 'b', 'c', 'c', 'c'])
# ['a', '2', 'b', 'c', '3']