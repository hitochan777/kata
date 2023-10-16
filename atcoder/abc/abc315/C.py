N = int(input())
ices = []
for _ in range(N):
  F, S = (int(x) for x in input().split())
  ices.append((S, F))

ices.sort(reverse=True)
def tastiness(a, b):
  if a[0] < b[0]:
    a, b = b, a
  # print(a,b)

  if a[1] == b[1]:
    return a[0] + b[0] // 2
  else:
    return a[0] + b[0]

# ans = tastiness(ices[0], ices[1])
# print(ices)
ans = 0
a = ices[0]
for i in range(1, N):
  b = ices[i]
  ans = max(tastiness(a, b), ans)

print(ans)
