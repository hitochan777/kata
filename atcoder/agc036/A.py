S = int(input())
ans = [0,0,10**9]
if S % (10**9) == 0:
  ans.append(0)
  ans.append(0)
  ans.append(S//(10**9))
else:
  ans.append(1)
  ans.append(10**9-S%(10**9))
  ans.append((S//(10**9))+1)
  

print(*ans)