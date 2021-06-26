N = int(input())
intervals = []
for _ in range(N):
  t, l, r = list(int(x) for x in input().split())
  intervals.append((t, l, r))

count = 0
for i in range(N):
  for j in range(i+1, N):
    a = intervals[i]
    b = intervals[j]
    if a[1] > b[1]:
      a, b = b, a
    
    overlap =  max(0, min(a[2], b[2]) - max(a[1], b[1]))
    not_included = a[0] in [2, 4] or b[0] in [3, 4]
    if a[2] == b[1]:
      if not_included:
        continue
      else:
        count += 1

    elif overlap > 0:
      count += 1

print(count)