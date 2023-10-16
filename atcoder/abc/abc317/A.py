N, H, X = (int(x) for x in input().split())
P = list(int(x) for x in input().split())
for i, p in enumerate(P):
  if H + p >= X:
    print(i+1)
    exit()