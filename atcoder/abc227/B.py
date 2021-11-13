N = int(input())
S = list(int(x) for x in input().split())
candidates = set()
for a in range(1, 1001):
  for b in range(1, 1001):
    candidates.add(4 * a * b + 3 * a + 3 * b)

count = sum(1 for s in S if s not in candidates)
print(count)