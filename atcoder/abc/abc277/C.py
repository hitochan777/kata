from atcoder.dsu import DSU
N = int(input())
nums = set()
nums.add(1)
ladders = []
for _ in range(N):
  A, B = (int(x) for x in input().split())
  nums.add(A)
  nums.add(B)
  ladders.append((A,B))

li = sorted(list(nums))
table = {n: i for i, n in enumerate(li)}

dsu = DSU(len(nums))
for a, b in ladders:
  dsu.merge(table[a], table[b])

for num in li[::-1]:
  if dsu.same(0, table[num]):
    print(num)
    exit()