def capacity(arr):
  if not arr or len(arr) < 3:
    return 0
  volume = 0
  left = 0
  right = len(arr) - 1
  l_max, r_max = arr[left], arr[right]

  while left < right:
    l_max, r_max = max(arr[left], l_max), max(arr[right], r_max)

    if l_max <= r_max:
      volume += l_max - arr[left]
      left += 1
    else:
      volume += r_max - arr[right]
      right -= 1

    print str(left) + ", " + str(right)

  return volume

print capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# 6