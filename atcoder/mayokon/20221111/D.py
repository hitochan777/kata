import math

N = int(input())
A = list(int(x) for x in input().split())
rgcd, lgcd = [A[0]], [A[-1]]

for i in range(1,N):
  rgcd.append(math.gcd(rgcd[-1], A[i]))

for i in range(N-2, -1, -1):
  lgcd.append(math.gcd(lgcd[-1], A[i]))

ans = max(rgcd[N-2], lgcd[N-2])
for i in range(1,N-1):
  tmp = math.gcd(rgcd[i-1], lgcd[N-i-2])
  ans = max(tmp, ans)

print(ans)
