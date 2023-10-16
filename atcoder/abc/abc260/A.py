from collections import Counter 
cnt = Counter(input())
for k, v in cnt.items():
  if v == 1:
    print(k)
    break
else:
  print(-1)

