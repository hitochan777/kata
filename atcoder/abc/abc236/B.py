from collections import Counter

N = int(input())
A = list(int(x) for x in input().split())

cnt = Counter(A)

for k, v in cnt.items():
  if v == 3:
    print(k)
    exit()