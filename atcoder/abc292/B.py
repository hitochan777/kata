from collections import defaultdict

N, Q = (int(x) for x in input().split())
cnt = defaultdict(int)
for _ in range(Q):
    c, x = (int(x) for x in input().split())
    if c == 1:
       cnt[x] += 1
    elif c == 2:
       cnt[x] += 2
    else:
       if cnt[x] >= 2:
          print("Yes")
       else:
          print("No")