import math
N = int(input())
AB = []
for i in range(N):
  a, b = (int(x) for x in input().split())
  AB.append((a + b, a, b))

AB.sort(reverse=True)
X = 0
for i in range(N):
  if i % 2 == 0:
    X += AB[i][1]
  else:
    X -= AB[i][2]

print(X)

    
