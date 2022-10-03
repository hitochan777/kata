N = int(input())
A = []
ans = 0
total = 0
for i in range(N):
  n = int(input())
  if n != 0:
    total += n
  else:
    ans += total // 2
    total = 0

ans += total // 2
print(ans)