H, W = (int(x) for x in input().split())
ans = 0
for _ in range(H):
  ans += input().count("#")

print(ans)