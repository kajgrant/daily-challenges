def hIndex(publications):
  return sum(i < j for i, j in enumerate(sorted(publications, reverse=True)))

print hIndex([5, 3, 3, 1, 0])
# 3