from collections import Counter
N, M = (int(x) for x in input().split())
A = Counter(int(x) for x in input().split())
B = Counter(int(x) for x in input().split())
if all(key in A and A[key] >= val for key, val in B.items()):
  print("Yes")
else:
  print("No")
  