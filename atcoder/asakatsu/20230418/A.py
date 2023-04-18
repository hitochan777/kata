N = int(input())
K = int(input())
xs = list(int(x) for x in input().split())
ans = 0
for x in xs:
  ans += min(x, K-x) * 2

print(ans)