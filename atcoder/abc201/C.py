S = input()
cnt = 0
for i in range(10**4):
  pw = str(i).zfill(4)
  for n, s in enumerate(S):
    if s == "o" and str(n) not in pw:
      break
    elif s == "x" and str(n) in pw:
      break
  else:
    cnt += 1

print(cnt)
