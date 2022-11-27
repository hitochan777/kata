import random
N = 2
Q = 6
print(N, Q)
num = N

for _ in range(Q):
  cmd = random.randint(1,3) 
  if cmd == 1:
    X, Y = 0, 0
    while X == Y:
      X = random.randint(1,N)
      Y = random.randint(1,N)

    print(cmd, X, Y)
  elif cmd == 2:
    X = random.randint(1,N)
    print(cmd, X)
    num += 1
  else:
    X = random.randint(1,num)
    print(cmd, X)

