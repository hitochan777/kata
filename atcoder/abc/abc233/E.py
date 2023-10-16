import sys
X = input()
s = sum(int(x) for x in X)
c = 0
ans = []
i = 0
while i < len(X) or c > 0:
  c += s
  ans.append(str(c % 10))
  c //= 10
  s -= int(X[len(X)-i-1])
  i += 1

sys.stdout.write("".join(ans[::-1]))