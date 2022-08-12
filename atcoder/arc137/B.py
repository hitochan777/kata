N = int(input())
A = list(int(x) for x in input().split())
mn, mx, cur, x, y = 0, 0, 0, 0, 0
for a in A:
  if a == 0:
    cur -= 1
  else:
    cur += 1

  x = min(x, cur-mx)
  y = max(y, cur-mn)
  mn = min(mn, cur)
  mx = max(mx, cur)

print(y-x+1)