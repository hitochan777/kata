S = input()
T = input()
N = len(T)

ng_cnt = 0
ok = [False] * N

def eq(a, b):
  return a == b or a == "?" or b == "?"

for i in range(N):
  a, b = T[i], S[len(S)-len(T)+i]
  ok[i] = eq(a,b)
  if not ok[i]:
    ng_cnt += 1

if ng_cnt == 0:
  print("Yes")
else:
  print("No")


for i in range(N):
  a, b  = S[i], T[i]
  new_ok = eq(a, b)
  if not ok[i] and new_ok:
    ng_cnt -= 1
  elif ok[i] and not new_ok:
    ng_cnt += 1

  ok[i] = new_ok

  if ng_cnt == 0:
    print("Yes")
  else:
    print("No")