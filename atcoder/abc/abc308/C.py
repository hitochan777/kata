from functools import cmp_to_key
def compare(A, B):
  a, b, _ = A
  c, d, _ = B
  x = a * (c+d)
  y = c * (a+b)
  return y - x

N = int(input())
li = []
for i in range(N):
  A, B = (int(x) for x in input().split())
  li.append((A, B, i+1))

li = sorted(li, key=cmp_to_key(compare))

ans = []
for val in li:
  ans.append(val[2])

print(*ans)