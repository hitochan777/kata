N = int(input())
li = []
for _ in range(N):
  x, y = (int(x) for x in input().split())
  li.append((x,y))

max_val = 0
for i in range(N):
  for j in range(i+1,N):
    max_val = max(max_val, (li[i][0] - li[j][0]) ** 2 + (li[i][1] - li[j][1]) ** 2)

print(max_val**0.5)