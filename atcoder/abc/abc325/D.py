N = int(input())
maxT = 0
products = []
for i in range(N):
  T, D = (int(x) for x in input().split())
  products.append((T, T+D))
  maxT = max(maxT, T+D)

products.sort()
cur = 0
ans = 0
t = 0
while cur < N and t < maxT+1:
  while cur < N:
    start, end = products[cur]
    t = max(start, t)
    if start <= t <= end:
      ans += 1
      cur += 1
      break
    elif end < t:
      cur += 1
    else:
      t += 1

  t += 1


# 10
# 4 1
# 1 2
# 1 4
# 3 2
# 5 1
# 5 1
# 4 1
# 2 1
# 4 1
# 2 4


# ---**-
# # ***---
# *****-
# --***-
# ----**
# ----**
# ---**-
# -**---
# ---**-
# -*****

print(ans)

  
  
