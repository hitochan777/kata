from collections import Counter

N = int(input())
A = list(int(x) for x in input().split())
cnt = Counter(A)

k = len(cnt)
if k % 2 == 1:
  print(k)
else:
  print(k-1)

