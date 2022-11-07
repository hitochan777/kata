def solve(N, K, S):
  c = S.count("1")
  ones = S[:K].count("1")
  zeros = S[:K].count("0")
  exists = False
  if ones == c and zeros == 0:
    exists = True

  for i in range(1,N-K):
    if S[i-1] == "1":
      ones -= 1
    elif S[i-1] == "0":
      zeros -= 1

    if S[i+K-1] == "1":
      ones += 1
    elif S[i+K-1] == "0":
      zeros += 1

    if ones == c and zeros == 0:
      if exists:
        return False

      exists = True

  return exists

T = int(input())
for _ in range(T):
  N, K = (int(x) for x in input().split())
  S = input()
  if solve(N, K, S):
    print("Yes")
  else:
    print("No")