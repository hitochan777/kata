N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
A.sort()
B.sort()
pa, pb = 0, 0
ans = 10**18
while pa < N and pb < M:
  a, b = A[pa], B[pb]
  ans = min(abs(a - b), ans)
  if ans == 0:
    break

  if a < b:
    pa += 1
  else:
    pb += 1

print(ans)
# 3 8 10 21
# 5 7 20