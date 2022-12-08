A, B, K = (int(x) for x in input().split())
i = 0
while A < B:
  A *= K
  i+=1

print(i)


