a, b, x = (int(x) for x in input().split())
ans = b // x
if a == 0:
  print(ans+1)
else:
  ans -= (a-1)//x
  print(ans)