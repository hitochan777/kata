from collections import defaultdict
N = int(input())

events = []
for _ in range(N):
  A, B = (int(x) for x in input().split())
  events.append((A, 1))
  events.append((A+B, -1))
  
events.sort()

ans = [0] * (N + 1)
cnt = 0
for i in range(len(events)-1):
  cnt += events[i][1]
  ans[cnt] += events[i+1][0] - events[i][0]

print(" ".join(map(str, ans[1:])))


