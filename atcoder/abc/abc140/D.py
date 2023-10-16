import re

N, K = (int(x) for x in input().split())
S = input()

Sp = re.sub("L+", "L", S)
Sp = re.sub("R+", "R", Sp)

gc = len(Sp) # group count
for _ in range(K):
  if gc >= 3:
    gc -= 2
  else:
    gc = 1

print(N - gc)