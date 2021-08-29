N = int(input())
seq = bin(N)

ans = "A"
for c in seq[3:]:
  if c == "0":
    ans += "B"
  else:
    ans += "BA"

print(ans)

