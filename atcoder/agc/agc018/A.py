import math

N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

def gcd(*nums):
  if len(nums) == 1:
    return nums[0]

  g = math.gcd(nums[0], nums[1])
  for i in range(2, len(nums)):
    g = math.gcd(g, nums[i])

  return g

g = gcd(*A)
mx = max(A)

if K <= mx and K % g == 0:
  print("POSSIBLE")
else:
  print("IMPOSSIBLE")
