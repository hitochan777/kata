H, W = (int(x) for x in input().split())
rows = []
for _ in range(H):
  A = input() 
  rows.append(A)

ans = []
for i in range(W):
  ans.append(sum(1 for j in range(H) if rows[j][i] == "#"))

print(*ans)