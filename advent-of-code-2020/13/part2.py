input()
nums = [(index, int(value)) for index, value in enumerate(input().split(",")) if value != "x"]

ts = nums[0][1]
period = nums[0][1]
for i in range(1, len(nums)):
  while (ts + nums[i][0]) % nums[i][1] != 0:
    ts += period

  period *= nums[i][1]

print(ts)

