from bisect import bisect_left
import math

N, M, P = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
B.sort()
acc = [0]
for b in B:
  acc.append(b + acc[-1])

ans = 0
# print(acc)
# print(B)
for a in A:
  t = P - a + 1
  idx = bisect_left(B, t)
  # print(idx)
  diff = acc[max(0, idx)] + (a * max(0, idx)) + P * max(0, M - idx)
  # print(diff)
  ans += diff

print(ans)