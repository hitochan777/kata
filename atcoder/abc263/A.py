nums = list(int(x) for x in input().split())
s = set(nums)
if len(s) != 2:
  print("No")
  exit()

arr = list(s)
a, b = nums.count(arr[0]), nums.count(arr[1])
a, b = sorted([a,b])
if a == 2 and b == 3:
  print("Yes")
else:
  print("No")