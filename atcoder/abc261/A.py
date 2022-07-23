l1, r1, l2, r2 = (int(x) for x in input().split())

cnt = 0
for i in range(0, 101):
  if l1 <= i <= r1 and l2 <= i <= r2:
    cnt += 1

print(max(cnt-1, 0))
