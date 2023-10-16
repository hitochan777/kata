import bisect

N, T = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
fs, ss = set(), set()
for i in range(2**(N>>1)):
  total = 0
  for j in range(N>>1):
    k = (i >> j) & 1
    if k == 1:
      total += A[j]

  fs.add(total)

for i in range(2**(N - (N>>1))):
  total = 0
  for j in range(N - (N>>1)):
    k = (i >> j) & 1
    if k == 1:
      total += A[(N >> 1) + j]

  ss.add(total)

first = sorted(list(fs))
second = sorted(list(ss))
max_val = 0
# print(first, second)
for num in first:
  if num > T:
    continue

  idx = bisect.bisect_left(second, T - num)
  # print(num,idx)
  if second[min(idx, len(second)-1)] + num <= T:
    max_val = max(max_val, second[min(idx, len(second)-1)] + num)

  if second[min(idx-1, len(second)-1)] + num <= T:
    max_val = max(max_val, second[min(idx-1, len(second)-1)] + num)

print(max_val)


