from atcoder.string import z_algorithm

N = int(input())
S = input()

ans = 0
for j in range(N):
  Z = z_algorithm(S[j:])
  for j, z in enumerate(Z):
    if z <= j:
      ans = max(ans, z)

print(ans)