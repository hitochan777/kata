from typing import Counter


N = int(input())
A = list(int(x) for x in input().split())
cnt = Counter(A)
B = list(set(A))
B.sort()
gb = 0
for k, v in cnt.items():
  if v >= 2:
    gb += v - 1

t = 0
i = 0
b = len(B)-1
while i < len(B) and b >= i:
  if B[i] == t+1:
    t += 1
    i += 1
  else:
    if gb >= 2:
      gb -= 2
      t += 1
    elif gb == 1 and B[b] > t+1:
      gb = 0
      b -= 1
      t += 1
    elif b-1 >= 0 and B[b-1] > t+1:
      t += 1
      b -= 2
    else:
      break

if gb > 0:
  t += gb // 2

print(t)