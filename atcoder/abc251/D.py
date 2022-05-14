W = int(input())

ans = []
for i in range(3):
  base = 100**i
  for j in range(1,100):
    ans.append(j * base)

print(len(ans))
print(*ans)