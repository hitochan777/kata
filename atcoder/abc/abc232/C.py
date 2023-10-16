# from collections import defaultdict

# N, M = (int(x) for x in input().split())
# a_cnt = defaultdict(int)
# b_cnt = defaultdict(int)
# for _ in range(M):
#   A, B = (int(x) for x in input().split())
#   a_cnt[A] += 1
#   a_cnt[B] += 1

# for _ in range(M):
#   C, D = (int(x) for x in input().split())
#   b_cnt[C] += 1 
#   b_cnt[D] += 1

# if sorted(list(a_cnt.values())) == sorted(list(b_cnt.values())):
#   print("Yes")
# else:
#   print("No")

from itertools import permutations
from collections import defaultdict

N, M = (int(x) for x in input().split())
ag = defaultdict(set)
bg = defaultdict(set)
for _ in range(M):
  A, B = (int(x) for x in input().split())
  ag[A].add(B)
  ag[B].add(A)

for _ in range(M):
  C, D = (int(x) for x in input().split())
  bg[C].add(D)
  bg[D].add(C)

ok = False
for p in permutations(range(1,N+1), N):
  if all(p[j-1] in bg[p[i-1]] for i in ag.keys() for j in ag[i]):
     ok = True
     break

print("Yes" if ok else "No") 