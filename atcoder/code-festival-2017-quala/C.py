from collections import Counter

H, W = (int(x) for x in input().split())
line = ""
for _ in range(H):
  line += input() 

cnt = Counter(line)
fours = (H // 2) * (W // 2)
while fours > 0:
  for key in cnt.keys():
    if cnt[key] >= 4:
      cnt[key] -= 4
      fours -= 1
      break
  else:
    print("No")
    exit()

twos = H // 2 if W % 2 == 1 else 0
while twos > 0:
  for key in cnt.keys():
    if cnt[key] >= 2:
      cnt[key] -= 2
      twos -= 1
      break
  else:
    print("No")
    exit()

twos = W // 2 if H % 2 == 1 else 0
while twos > 0:
  for key in cnt.keys():
    if cnt[key] >= 2:
      cnt[key] -= 2
      twos -= 1
      break
  else:
    print("No")
    exit()

rem = sum(cnt.values())
if H % 2 == 1 and W % 2 == 1:
  target = 1
else:
  target = 0

if rem == target:
  print("Yes")
else:
  print("No")