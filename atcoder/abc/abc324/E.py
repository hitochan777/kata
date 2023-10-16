from bisect import bisect_left
N, T = input().split()
revT = T[::-1]
N = int(N)

L = []
R = []

def find_idx(S, pattern):
  i = 0
  j = 0
  while i < len(S) and j < len(pattern):
    if S[i] == pattern[j]:
      j += 1

    i += 1

  # print(S, pattern, j)
  return j 

for _ in range(N):
  S = input()
  L.append(find_idx(S, T))
  R.append(find_idx(S[::-1], revT))

# subtract = sum(1 for l, r in zip(L, R) if l + r >= len(T))

# print(L)
# print(R)

# L.sort()
R.sort()

ans = 0
for l in L:
  idx = bisect_left(R, len(T) - l)
  ans += N - idx

# ans -= subtract
print(ans)