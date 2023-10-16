N = int(input())
li = []
for _ in range(N):
  w = int(input())
  min_val = 10**6
  min_idx = None
  for i, item in enumerate(li):
    if item < w:
      continue

    min_val = min(item - w, min_val)
    if min_val == item - w:
      min_idx = i

  if min_idx is None:
    li.append(w)
  else:
    li[min_idx] = w

print(len(li))