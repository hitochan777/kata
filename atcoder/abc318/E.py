from collections import defaultdict
N = int(input())
A = list(int(x) for x in input().split())
left = defaultdict(int)
right = defaultdict(int)
left[A[0]] += 1
for a in A[2:]:
  right[a] += 1

total = sum(left[i] * right[i] for i in range(1, N+1))
ans = 0
for i in range(1, N-1):
  a, b, c = A[i-1:i+2]
  ans += total - left[b] * right[b]
  for j in set([b, c]):
    total -= left[j] * right[j]

  right[c] -= 1
  left[b] += 1
  # print(left, right)

  for j in set([b, c]):
    total += left[j] * right[j]

print(ans)