from collections import defaultdict
N = int(input())
s = set()
for _ in range(N):
  S = input()
  R = S[::-1]
  if S > R:
    S, R = R, S

  s.add((S,R))

print(len(s))