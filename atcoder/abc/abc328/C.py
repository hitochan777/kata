N, Q = (int(x) for x in input().split())
S = input()
acc = [0]
for i in range(N-1):
  next = acc[-1] + (1 if S[i] == S[i+1] else 0)
  acc.append(next)

for _ in range(Q):
  l, r = (int(x) for x in input().split())
  print(acc[r-1] - acc[l-1])