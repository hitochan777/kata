from itertools import permutations
N = int(input())
P = tuple(int(x) for x in input().split())
Q = tuple(int(x) for x in input().split())

a, b = 0, 0
pm = sorted(list(permutations(range(1,N+1))))
for i, A in enumerate(pm, start=1):
  if A == P:
    a = i
    break

for i, A in enumerate(pm, start=1):
  if A == Q:
    b = i
    break

print(abs(a-b))