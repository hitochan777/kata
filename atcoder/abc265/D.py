from bisect import bisect_left

N, P, Q, R = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
acc = [0]
for a in A:
  acc.append(acc[-1]+a)

for i in range(N):
  cur = acc[i]
  for val in [P, Q, R]:
    target = val + cur
    idx = bisect_left(acc, target)
    if idx >= len(acc):
      break

    if acc[idx] != target:
      break

    cur = acc[idx]
  else:
    print("Yes")
    exit()

print("No")