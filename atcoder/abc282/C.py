N = int(input())
S = input()
sured = False
ans = []
for c in S:
  if c == "\"":
    sured = not sured

  if c == "," and not sured:
    ans.append(".")
  else:
    ans.append(c)

print("".join(ans))
