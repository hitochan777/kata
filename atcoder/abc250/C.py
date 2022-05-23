N, Q = (int(x) for x in input().split())
indices = list(range(N))
nums = list(range(N))
for _ in range(Q):
  x = int(input())-1
  idx = indices[x]
  if idx == N - 1:
    indices[x], indices[nums[idx-1]] = indices[nums[idx-1]], indices[x]
    nums[idx], nums[idx-1] = nums[idx-1], nums[idx]
  else:
    indices[x], indices[nums[idx+1]] = indices[nums[idx+1]], indices[x]
    nums[idx], nums[idx+1] = nums[idx+1], nums[idx]

print(*[num + 1 for num in nums])