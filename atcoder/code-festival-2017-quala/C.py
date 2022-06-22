from collections import Counter

H, W = (int(x) for x in input().split())
line = ""
for _ in range(H):
  line += input() 

cnt = Counter(line)
for key in cnt.keys():
  cnt[key] %= 4

if H % 2 == 1:
  for key in cnt.keys():
    cnt[key] %= 2

if W % 2 == 1:
  for key in cnt.keys():
    cnt[key] %= 2

rem = sum(cnt.values())
if H % 2 == 1 & W % 2 == 1:
  target = 1
else:
  target = 0

if rem == target:
  print("Yes")
else:
  print("No")