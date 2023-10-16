N = int(input())

Fs = []
for _ in range(N):
  F = int("".join(input().split()), 2)
  Fs.append(F)

Ps = []
for _ in range(N):
  P = list(int(x) for x in input().split())
  Ps.append(P)

max_profit = -10**18
for i in range(1, 1 << 10):
  profit = sum(Ps[j][bin(i & f).count("1")] for j, f in enumerate(Fs))
  max_profit = max(max_profit, profit)

print(max_profit)
    