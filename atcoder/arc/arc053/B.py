from collections import Counter
S = input()
cnt = Counter(S)
N = len(S)
K = sum(1 for k, v in cnt.items() if v % 2 == 1)
if K == 0:
  print(N)
else:
  print((N - K) // (2 * K) * 2 + 1)