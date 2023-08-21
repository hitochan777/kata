# AxxxxxB CxxxxxD
# A = D
# B = C

from collections import defaultdict

cnt = defaultdict(int)
N = int(input())
for i in range(1, N+1):
  s = str(i)
  cnt[(int(s[0]), int(s[-1]))] += 1

ans = 0
for i in range(1, 10):
  for j in range(1, 10):
    ans += cnt[(i, j)] * cnt[(j, i)]

print(ans)
