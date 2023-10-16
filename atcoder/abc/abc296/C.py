from collections import Counter
N, X = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
cnt = Counter(A)

for a in A:
  b = a - X
  if cnt[b] > 0:
    print("Yes")
    exit()

  b = a + X
  if cnt[b] > 0:
    print("Yes")
    exit()

print("No")