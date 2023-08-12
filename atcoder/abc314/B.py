N = int(input())

ss = []
for _ in range(N):
  C = int(input())
  s = set(list(int(x) for x in input().split()))
  ss.append(s)

X = int(input())
nums = []
for i, s in enumerate(ss):
  if X in s:
    nums.append((len(s), i))

if len(nums) == 0:
  print(0)
  exit()

n, _ = min(nums)
ids = []
for l, i in nums:
  if l == n:
    ids.append(i+1)

ids.sort()
print(len(ids))
print(*ids)



