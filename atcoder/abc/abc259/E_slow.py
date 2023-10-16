from math import gcd

N = int(input())
nums = []
for _ in range(N):
  m = int(input())
  n = 1
  for _ in range(m):
    p, e = (int(x) for x in input().split())
    n *= p**e

  nums.append(n)
  
ans = set()
for i in range(N):
  targets = [n for j, n in enumerate(nums) if i != j]
  lcm = 1
  for target in targets:
    lcm = lcm*target//gcd(lcm, target)
  
  if lcm != 1 and lcm not in ans:
    print(i+1)
    ans.add(lcm)

print(len(ans))

    