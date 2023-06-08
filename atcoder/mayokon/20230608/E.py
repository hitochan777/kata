from collections import defaultdict

neg = defaultdict(lambda: 10**18)
pos = defaultdict(lambda: -10**18)

nums = set()
N = int(input())
for _ in range(N):
  X, C = (int(x) for x in input().split())
  if X >= 0:
    pos[C] = max(X, pos[C])
  else:
    neg[C] = min(X, neg[C])

  nums.add(C)

pos[0] = 0
neg[0] = 0

nums = sorted([0] + list(nums))
pos_best, neg_best = 0, 0
print(nums)
for i in range(len(nums)-1):
  cur_num = nums[i+1]
  prev_num = nums[i]
  a, b, c, d, e = [0] * 5
  if cur_num in pos:
    a, d = pos_best + abs(pos[prev_num] - pos[cur_num]), neg_best + abs(neg[prev_num] - pos[cur_num])

  if cur_num in neg:
    c, e = neg_best + abs(neg[prev_num] - neg[cur_num]), pos_best + abs(pos[prev_num] - neg[cur_num]) 

  if cur_num in pos and cur_num in neg:
    b = abs(pos[cur_num] - neg[cur_num])

  print(a, b, c, d, e)

  post_best = min(a+2*b, e+b, d+2*b, c+b)
  neg_best = min(a+b, e+2*b, d+b, c+2*b)

print(min(pos_best, neg_best))

