N = int(input())

def ok(n):
  nums = list(str(n))
  if len(nums) != 3:
    return False

  return int(nums[0]) * int(nums[1]) == int(nums[2])

for i in range(N, 1000):
  if ok(i):
    print(i)
    exit()