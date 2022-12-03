N = int(input())
A = list(int(x) for x in input().split())

axor = [0]
asum = [0]
for a in A:
  axor.append(axor[-1]^a)
  asum.append(asum[-1]+a)

r = 0
ans = 0
for l in range(N):
  r = l
  while r < N and (asum[r+1] - asum[l]) == (axor[r+1] - axor[l]):
    r += 1

  ans += r - l

print(ans)