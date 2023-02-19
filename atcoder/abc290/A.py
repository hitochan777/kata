N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = list(int(x)-1 for x in input().split())
ans = 0
for b in B:
  ans += A[b]

print(ans)