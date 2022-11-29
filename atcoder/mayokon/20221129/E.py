from bisect import bisect_left
A, B, Q = (int(x) for x in input().split())
S, T = [], []
for _ in range(A):
  s = int(input())
  S.append(s)

for _ in range(B):
  t = int(input())
  T.append(t)

def search(arr, x, left):
  # print("arr", arr)
  idx = bisect_left(arr, x)
  if idx == len(arr):
    idx -= 1

  # print(idx)
  if left:
    if arr[idx] > x:
      idx -= 1

    if idx >= 0:
      return arr[idx]
    else:
      return None
  else:
    if arr[idx] < x:
      idx += 1

    if idx < len(arr):
      return arr[idx]
    else:
      return None

# print(S)
# print(T)
# print(x2)
for _ in range(Q):
  ans = 10**18
  x = int(input())
  for S, T in [[S, T], [T,S]]:
    for l1 in [True, False]:
      for l2 in [True, False]:
        x2 = search(S, x, l1)
        if x2 is None:
          continue

        d = abs(x-x2)
        x3 = search(T, x2, l2)
        # print(x, x2, x3)
        if x3 is None:
          continue
        d += abs(x2-x3)
        ans = min(d, ans)

  print(ans)
