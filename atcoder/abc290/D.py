import math
T = int(input())
for _ in range(T):
  N, D, K = (int(x) for x in input().split())
  D %= N
  if D == 0:
    print(K-1)
  elif D == N-1:
    if K == 1:
      print(0)
    elif K == 2:
      print(N-1)
    else:
      print(N-2-(K-3))
  else:
    C = math.ceil(N / D)
    ans = (K-1) // C + ((K-1) % C) * D
    print(ans)