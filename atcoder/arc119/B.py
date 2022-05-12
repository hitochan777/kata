N = int(input())
S = input()
T = input()

sa = [i for i, c in enumerate(S) if c == "0"]
ta = [i for i, c in enumerate(T) if c == "0"]
if len(sa) != len(ta):
  print(-1)
  exit()

ans = sum(1 for a, b in zip(sa, ta) if a != b)
print(ans)