N, Q = (int(x) for x in input().split())
A = list(range(N))
pos = list(range(N))
for _ in range(Q):
  x = int(input())-1
  if pos[x] == N-1:
    nb = pos[x] - 1
    A[pos[x]], A[nb] = A[nb], A[pos[x]]
    # pos[x], pos[A[pos[x]]] = nb, pos[x]
    pos[A[pos[x]]] = pos[x]
    pos[x] = nb
  else:
    nb = pos[x] + 1
    A[pos[x]], A[nb] = A[nb], A[pos[x]]
    # print(x, A[pos[x]], nb, pos[x])
    # print(pos)
    pos[A[pos[x]]] = pos[x]
    pos[x] = nb
    # print(pos)

  # print(*[a+1 for a in A])

print(*[a+1 for a in A])
