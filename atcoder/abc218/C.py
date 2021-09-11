import numpy as np

N = int(input())
S = list()
T = list()

empty_line = "." * N

def remove_redundant(S):
  new_S = []
  for s in S:
    if s == empty_line and len(new_S) == 0:
      continue

    new_S.append(s)

  S = new_S
  new_S = []
  for s in reversed(S):
    if s == empty_line and len(new_S) == 0:
      continue 

    new_S.append(list(s))

  return new_S

for _ in range(N):
  line = input()
  S.append(line)

S = remove_redundant(S)

for _ in range(N):
  line = input()
  T.append(list(line)) 

T = remove_redundant(T)

S = np.array(S)
T = np.array(T)



S = S.transpose().tolist()
T = T.transpose().tolist()
S = ["".join(s) for s in S]
S = ["".join(t) for t in T]
S = remove_redundant(S)
T = remove_redundant(T)
print(S)
print(T)

S = np.array(S)
T = np.array(T)

ok = False
for _ in range(4):
  S = np.rot90(S)
  if S.shape != T.shape:
    continue
  
  if (S == T).all():
    ok = True
    break

print("Yes" if ok else "No")
