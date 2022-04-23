from collections import Counter
N = int(input())
cnt = Counter(int(x) for x in input().split())
nums = sorted(cnt.keys())
# print(nums)
ans = 0
n = len(nums)
i = 0
while i < n and nums[i] * nums[i] <= nums[-1]:
  j = i
  while j < n and nums[i] * nums[j] <= nums[-1]:
    mul = nums[i] * nums[j]
    if mul in cnt:
      # print(nums[i], nums[j], mul, cnt[nums[i]], cnt[nums[j]],  cnt[mul])
      delta = cnt[nums[i]] * cnt[nums[j]] * cnt[mul]
      if (i != j):
        delta *= 2

      ans += delta

    j += 1

  i += 1

print(ans)