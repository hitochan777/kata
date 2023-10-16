N, K = (int(x) for x in input().split())

ans = (N // K) ** 3
if K % 2 == 0:
  l = (N - (K // 2)) // K + 1
  ans += l**3

print(ans)