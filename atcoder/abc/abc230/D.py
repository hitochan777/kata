N, D = (int(x) for x in input().split())
intervals = []
for _ in range(N):
  L, R = (int(x) for x in input().split())
  intervals.append((R, L))

intervals.sort()

def overlap(p1, p2):
  return p1[0] <= p2[1] and p2[0] <= p1[1]

cnt = 0
i = 0
while i < N:
  R, L = intervals[i]
  j = i + 1
  while j < N:
    R2, L2 = intervals[j]
    if overlap((R, R + D-1), (L2, R2)):
      j += 1
    else:
      break

  i = j

  cnt += 1

print(cnt)