N = int(input())
cnt = 0
c1, c2, c3 = 0, 0, 0
for _ in range(N):
  s = input()
  cnt += s.count("AB")
  if s[0] == "B" and s[-1] == "A":
    c1 += 1
  elif s[0] == "B":
    c2 += 1
  elif s[-1] == "A":
    c3 += 1

if c1:
    cnt += c1 + min(c2, c3) if c2 + c3 > 0 else c1 - 1
else:
    cnt += min(c2, c3)

print(cnt)