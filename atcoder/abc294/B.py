H, W = (int(x) for x in input().split())
for _ in range(H):
  S = list(int(x) for x in input().split())
  ans = []
  for c in S:
    if c == 0:
      ans.append(".")
    else:
      ans.append(chr(ord("A") + c - 1))

  print("".join(ans))
