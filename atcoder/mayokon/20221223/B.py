from collections import Counter
cnt = Counter(input())
if all(v % 2 == 0for v in cnt.values()):
  print("Yes")
else:
  print("No")
