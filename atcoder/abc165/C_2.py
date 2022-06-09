from collections import deque

N, M, Q = (int(x) for x in input().split())
reqs = []
for _ in range(Q):
  a,b,c,d = (int(x) for x in input().split())
  a -= 1
  b -= 1
  reqs.append((a,b,c,d))

def get_score(A):
  return sum(d for a,b,c,d in reqs if A[b] - A[a] == c)
  

q = deque()
ans = 0
for i in range(1,M+1):
  q.append([i])

while len(q) > 0:
  A = q.pop()
  if len(A) == N:
    ans = max(ans, get_score(A))
    continue

  for i in range(A[-1], M+1):
    q.append([*A, i])

print(ans)

