N = int(input())
intervals = []
ans = []
for _ in range(N):
  L, R = (int(x) for x in input().split())
  intervals.append((L,R))

intervals.sort()
i = 0
while i < N:
  L, R = intervals[i]
  while i + 1 < N:
    L1, R1 = intervals[i+1]
    if R < L1:
      break

    R = max(R, R1)
    i += 1

  ans.append((L,R))
  i += 1

for L, R in ans:
  print(L, R)