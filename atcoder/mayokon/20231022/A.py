X, N = (int(x) for x in input().split())
p = set(list(int(x) for x in input().split()))

argmin = 10**18
ans = 0
for i in range(102):
  diff = abs(i - X)
  if i not in p and diff < argmin:
    argmin = diff
    ans = i

print(ans)

