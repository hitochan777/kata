N, W = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

s = set()
for i in range(N):
  if A[i] <= W:
    s.add(A[i])

for i in range(N):
  for j in range(i+1, N):
    total = A[i] + A[j]
    if total <= W:
      s.add(total)

for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      total = A[i] + A[j] + A[k]
      if total <= W:
        s.add(total)

print(len(s))