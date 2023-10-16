from itertools import permutations

def ok(Ts):
  for i in range(len(Ts)-1):
    diff = sum(1 for a, b in zip(Ts[i], Ts[i+1]) if a != b)
    if diff != 1:
      return False

  return True

N, M = (int(x) for x in input().split())
S = []
for _ in range(N):
  S.append(input())

for p in permutations(range(N)):
  if ok([S[i] for i in p]):
    print("Yes")
    exit()

print("No")