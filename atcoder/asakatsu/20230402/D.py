N = int(input())
nums = []
for _ in range(N):
    d = int(input())
    nums.append(d)

nums.sort(reverse=True)
mx = sum(nums)
mn = max(0, nums[0] - sum(nums[1:]))
print(mx)
print(mn)