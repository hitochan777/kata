# partially taken from https://note.nkmk.me/python-union-find/ 
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

n, m = list(map(int, input().split()))
uf = UnionFind(n)
for _ in range(m):
    a, b = list(map(int, input().split()))
    uf.union(a-1, b-1)

counts = list(map(lambda item: len(item[1]), uf.all_group_members().items()))
print(max(counts))
