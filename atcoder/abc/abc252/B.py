N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
maxA = max(A)

nums = set([i + 1 for i, a in enumerate(A) if a == maxA])
if any([(b in nums) for b in B]):
  print("Yes")
else:
  print("No")