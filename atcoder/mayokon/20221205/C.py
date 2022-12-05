from collections import Counter
N = int(input())
S = []
for _ in range(N):
  S.append([int(x) for x in list(input())])

ans = 10**18
for i in range(10):
  cnt = Counter(sorted([s.index(i) for s in S]))
  val = 0
  for k, v in cnt.items():
    val = max(val,k+(v-1)*10)
  
  ans = min(ans, val)

print(ans)