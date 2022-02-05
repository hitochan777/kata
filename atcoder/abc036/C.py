N = int(input())
s = set()
nums = []
for _ in range(N):
  a = int(input())
  s.add(a)
  nums.append(a)

d = {val: i for i, val in enumerate(sorted(list(s)))}
for num in nums:
  print(d[num])