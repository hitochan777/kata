N, K = (int(x) for x in input().split())
X = [int(x) for x in input().split()]
p, q = 0, 0
def get_time(start, end):
  if start * end >= 0:
    return max(abs(start), abs(end))

  return min(abs(start), abs(end)) + abs(start) + abs(end)

ans = 10**18
while p < N and q < N:
  if q - p + 1 == K:
    t = get_time(X[p], X[q])
    ans = min(t, ans)
    p += 1
  else:
    q += 1

print(ans)



