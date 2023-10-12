N = int(input())

used = set()
ans = 0
arg_max = None
for i in range(N):
  S, T = input().split()
  T = int(T)
  if S not in used:
    if ans < T:
      ans = T
      arg_max = i + 1

    used.add(S)

print(arg_max)
