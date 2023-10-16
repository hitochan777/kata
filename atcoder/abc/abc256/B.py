N = int(input())
A = list(int(x) for x in input().split())
vals = [False] * 4

ans = 0
for a in A:
  vals[0] = True
  for i in range(3, -1, -1):
    if not vals[i]:
      continue

    vals[i] = False
    if i + a >= 4:
      ans += 1
    else:
      vals[i+a] = True

print(ans)
