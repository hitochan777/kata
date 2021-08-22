N = int(input())

acc = [[0], [0]]
for i in range(N):
  C, P = (int(x) for x in input().split())
  acc[C-1].append(P + acc[C-1][-1])
  acc[C%2].append(acc[C%2][-1])

Q = int(input())
for _ in range(Q):
  L, R = (int(x) for x in input().split())
  print(acc[0][R]-acc[0][L-1], acc[1][R]-acc[1][L-1])