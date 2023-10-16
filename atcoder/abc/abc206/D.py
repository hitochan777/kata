from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

N = int(input())
A = list(map(int, input().split()))
uf = UnionFind(2 * 10**5)
count = 0
for i in range(N // 2):
  if uf.find(A[i]-1) == uf.find(A[N-i-1]-1):
    continue

  uf.union(A[i]-1, A[N-i-1]-1)
  count += 1

print(count)