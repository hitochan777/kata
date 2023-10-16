N = int(input())
strs = []
def solve(strs, i):
  used = set()
  for str in strs:
    idx = str.find(i)
    while idx in used:
      idx += 10
    
    used.add(idx)

  return max(used)

for _ in range(N):
  S = input()
  strs.append(S)

ans = 10**18
for i in range(10):
  ans = min(ans, solve(strs, str(i)))

print(ans)