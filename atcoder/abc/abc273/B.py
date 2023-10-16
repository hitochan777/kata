X, K = (int(x) for x in input().split())

for i in range(K):
  r = X % (10**(i+1))
  X -= r
  if r // (10**i) >= 5:
    X += 10**(i+1)

print(X)
    
