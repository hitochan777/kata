N = int(input())
S = list(int(x) for x in input().split())

x = [0, 0]
for i in range(N):
  x.append(S[i] - x[-1] - x[-2])

c1 = -min(x[::3])
c2 = -min(x[1::3])
c3 = min(x[2::3])
if c1 + c2 > c3:
  print("No")
  exit()

print("Yes")
a = c1
b = c2
ans = []
for i in range(N+2):
  if i % 3 == 0:
    ans.append(x[i] + a)
  elif i % 3 == 1:
    ans.append(x[i] + b)
  else:
    ans.append(x[i] - a - b)

print(*ans)