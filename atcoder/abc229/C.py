N, W = (int(x) for x in input().split())
nums = []
for _ in range(N):
  a, b = (int(x) for x in input().split())
  nums.append((a, b))

nums.sort(reverse=True)
total = 0
i = 0
while W > 0 and i < N:
  a, b = nums[i]
  diff = min(W, b)
  W -= diff
  total += diff * a
  i += 1

print(total)
