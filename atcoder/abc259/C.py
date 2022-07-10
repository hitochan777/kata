S = input()
T = input()

def dedup(s):
  sp = []
  cnt = 1
  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      cnt += 1
    else:
      sp.append((s[i], cnt))
      cnt = 1

  sp.append((s[-1], cnt))

  return sp

Sp = dedup(S)
Tp = dedup(T)
# print(Sp, Tp)

if len(Sp) != len(Tp):
  print("No")
  exit()

for s, t in zip(Sp, Tp):
  if s[0] != t[0]:
    print("No")
    exit()

  if s[1] > t[1]:
    print("No")
    exit()

  if s[1] == t[1]:
    continue

  if s[1] < t[1]:
    if s[1] == 1:
      print("No")
      exit()

print("Yes")
