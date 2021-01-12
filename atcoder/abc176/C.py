n = int(input())
nums = list(map(int, input().split()))
total = 0
mx = 0
for i in range(n):
    total += max(0, mx - nums[i])
    mx = max(nums[i], mx)

print(total)