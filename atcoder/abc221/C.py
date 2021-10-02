N = input()
d = len(N)

max_val = 0
for i in range(1,(1 << d) - 1):
  nums = ["", ""]
  for j in range(d):
    nums[(i >> j)&1] += N[j]

  num1 = int("".join(sorted(nums[0], reverse=True)))
  num2 = int("".join(sorted(nums[1], reverse=True)))
  max_val = max(max_val, num1 * num2)

print(max_val)