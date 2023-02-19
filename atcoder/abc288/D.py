N, K = (int(x) for x in input().split())
A = [int(x) for x in input().split()]

acc = [[0] for _ in range(K)]
for i in range(N):
  for k in range(K):
    acc[k].append(acc[k][-1]+(A[i] if i % K == k else 0))

Q = int(input())
for _ in range(Q):
  l, r = (int(x) for x in input().split())
  base = acc[0][r] - acc[0][l-1]
  if all(acc[i][r] - acc[i][l-1] == base for i in range(1, K)):
    print("Yes")
  else:
    print("No")
  