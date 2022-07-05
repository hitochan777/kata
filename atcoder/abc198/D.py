from itertools import permutations

S1 = input()
S2 = input()
S3 = input()

s = list(set(list(S1 + S2 + S3)))
d = {c: i for i, c in enumerate(s)}
D1 = [d[c] for c in S1]
D2 = [d[c] for c in S2]
D3 = [d[c] for c in S3]
if len(s) > 10:
  print("UNSOLVABLE")
  exit()


for perm in permutations(range(10)):
  n1 = 0
  for i in D1:
    n1 = 10 * n1 + perm[i]

  n2 = 0
  for i in D2:
    n2 = 10 * n2 + perm[i]

  n3 = 0
  for i in D3:
    n3 = 10 * n3 + perm[i]

  if n1 == 0 or n2 == 0 or n3 == 0:
    continue

  if len(S1) != len(str(n1)) or len(S2) != len(str(n2)) or len(S3) != len(str(n3)):
    continue

  if n1 + n2 == n3:
    print(n1)
    print(n2)
    print(n3)
    exit()


print("UNSOLVABLE")
