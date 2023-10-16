N = int(input())
S = [input(), input()]
MOD = 1000000007

prev_vert = False
i = 0
ans = 1
while i < N:
  is_vert = S[0][i] == S[1][i]
  if is_vert:
    if i == 0:
      ans *= 3
    elif prev_vert:
      ans *=2
    else:
      ans *= 1

    i += 1

  else:
    if i == 0:
      ans *= 6
    elif prev_vert:
      ans *= 2
    else:
      ans *= 3

    i += 2

  ans %= MOD

  prev_vert = is_vert

print(ans)