from itertools import permutations

def fn(n, m):
  if m == 0:
    return [[]]
  if m == 1:
    return [[n]]

  arrs = []
  for i in range(n-m+1):
    for arr in fn(n-i-1, m-1):
      arrs.append([i+1] + arr)

  return arrs


N, M = (int(x) for x in input().split())
S = []
sum_len = 0
for _ in range(N):
  s = input()
  S.append(s) 
  sum_len += len(s)

T = set()
for _ in range(M):
  T.add(input()) 

for ps in permutations(range(N)):
  strs = [S[p] for p in ps]
  for i in range(N-1, 16-sum_len+1):
    arrs = fn(i, N-1)
    for arr in arrs:
      X = strs[0]
      for j in range(N-1):
        X += "_" * arr[j]
        X += strs[j+1]

      if X not in T and 3 <= len(X) <= 16:
        print(X)
        exit()

print(-1)