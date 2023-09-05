import heapq
X, Y, Z, K = (int(x) for x in input().split())
sizes = [X, Y, Z]
A = sorted(list(int(x) for x in input().split()), reverse=True)
B = sorted(list(int(x) for x in input().split()), reverse=True)
C = sorted(list(int(x) for x in input().split()), reverse=True)

q = [(-(A[0] + B[0] + C[0]), (0, 0, 0))]
visited = set()
cnt = 0
while q:
  taste, vals = heapq.heappop(q)
  print(-taste)
  cnt += 1
  if cnt >= K:
    break

  for i in range(3):
    if vals[i] + 1 < sizes[i]:
      new_vals = list(vals)
      new_vals[i] += 1
      if tuple(new_vals) in visited:
        continue

      visited.add(tuple(new_vals))
      heapq.heappush(q, (-(A[new_vals[0]] + B[new_vals[1]] + C[new_vals[2]]), tuple(new_vals)))


  
