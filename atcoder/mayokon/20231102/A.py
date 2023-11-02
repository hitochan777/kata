H, W = (int(x) for x in input().split())
ans = ["*" * (W+2)]
for _ in range(H):
  row = "*" + input() + "*"
  ans.append(row)

ans.append("*" * (W+2))
print("\n".join(ans))