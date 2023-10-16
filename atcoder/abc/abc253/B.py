H, W = (int(x) for x in input().split())
li = []
for i in range(H):
  S = input()
  for j, c in enumerate(S):
    if c == "o":
      li.append((i, j))
  
print(abs(li[0][0] - li[1][0]) + abs(li[0][1] - li[1][1]))