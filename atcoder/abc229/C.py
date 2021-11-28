N, W = (int(x) for x in input().split())
nums = []
for _ in range(N):
  a, b = (int(x) for x in input().split())
  nums.append((b, a))

nums.sort(reverse=True)
total = 0
for b, a in nums:
  diff = min(W, a)
  W -= diff
  if W == 0:
    break

  total += diff * b

print(total)
