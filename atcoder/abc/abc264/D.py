S = input()
A = "atcoder"

ans = 0
nums = []
for c in S:
  idx = A.find(c)
  nums.append(idx)

ans = 0
for i, num in enumerate(nums):
  ans += sum(1 for j in range(i) if nums[j] > num)
    
print(ans)