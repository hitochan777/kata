N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

X = 0
nums = []
sums = [0]
visited = set()
visited.add(0)
while True:
  nums.append(A[X])
  X += A[X]
  X %= N
  if X in visited:
    break

  sums.append(X)
  visited.add(X)

idx = sums.index(X)
repeating_sum = sum(nums[idx:])
ans = 0
for i in range(min(K, idx+1)):
  ans += nums[i]

print(K, idx, nums)
for i in range(max(K-(idx+1), 0) % (len(nums)-idx+1)):
  ans += nums[idx+i]

ans += repeating_sum * (max(K-(idx+1), 0) // (len(nums)-idx+1))
print(ans)