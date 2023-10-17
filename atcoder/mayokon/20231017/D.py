from collections import defaultdict

N = int(input())
vals = set()
history = []
for _ in range(N):
  A, B = (int(x) for x in input().split())
  vals.add(A)
  vals.add(A+B-1)
  history.append((A, A+B-1))

vals.add(0)
vals.add(10**10)
vals = sorted(list(vals))
m = {v:i for i, v in enumerate(vals)}
count = [0] * len(vals)
for i in range(N):
  a, b = history[i]
  count[m[a]] += 1
  count[m[b]+1] -= 1

# print(count)
for i in range(len(count)-1):
  count[i+1] += count[i]

cnt = defaultdict(int)
for i in range(1, len(count)-1):
  # print(count[i], vals[i+1], vals[i])
  if count[i] == count[i+1]:
    cnt[count[i]] += vals[i+1] - vals[i]
  else:
    cnt[count[i]] += 1

# print(vals)
# print(count)
ans = []
for i in range(1, N+1):
  ans.append(cnt[i])

print(*ans)
