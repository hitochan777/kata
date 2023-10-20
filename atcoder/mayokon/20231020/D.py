import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

deps = defaultdict(set)

N = int(input())
for i in range(1, N+1):
  C, *P = (int(x) for x in input().split())
  deps[i] = set(P)

# print(deps)
visited = set()
requirements = []

def dfs(book, visited, requirements):
  if book in visited:
    return

  visited.add(book)
  for dep in deps[book]:
    dfs(dep, visited, requirements)

  requirements.append(book)

dfs(1, visited, requirements)
print(*requirements[:-1])

