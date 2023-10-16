import sys

sys.setrecursionlimit(1000000)

N, X = (int(x) for x in input().split())
num_list = []

def count(cur, num_list, i):
  if i == N - 1:
    return sum(1 for a in num_list[i] if cur * a == X)
          
  total = 0
  for a in num_list[i]:
    total += count(cur * a, num_list, i+1)

  return total

for _ in range(N):
  L, *A = (int(x) for x in input().split())
  num_list.append(A)

print(count(1, num_list, 0))