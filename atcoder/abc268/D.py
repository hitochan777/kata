from itertools import permutations

def get_combs(K, N):
  if N <= 1:
    return [[K]]
  
  combs = []
  for i in range(1, K):
    for c in get_combs(K-i, N-1):
      combs.append([i] + c)
  
  return combs


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

# print(list(permutations(range(N))))
for p in permutations(range(N)):
  for i in range(N-1, 16-sum_len+1):
    for comb in get_combs(i, N-1):
      X = S[p[0]]
      for j, val in enumerate(p[1:]):
        X += ("_" * comb[j]) + S[val]

      if len(X) < 3:
        continue

      if X not in T:
        print(X)
        exit()

print(-1)
