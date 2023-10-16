N = int(input())
S = input()
cnt = 0

max_val = 0
for c in S:
  if c == "(":
    cnt += 1
  else:
    cnt -= 1

  max_val = max(max_val, -cnt)

S = "(" * max_val + S
cnt = 0
for c in S:
  if c == "(":
    cnt += 1
  else:
    cnt -= 1

S = S + ")" * cnt

print(S)