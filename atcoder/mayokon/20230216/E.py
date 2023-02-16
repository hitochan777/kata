W = int(input())

ans = []
for d in [100**0, 100**1, 100**2]:
  for i in range(1, 100):
    ans.append(d * i)

ans.append(10**6)
print(len(ans))
print(*ans)

