N = int(input())

divs = []
for i in range(1, 10):
  if N % i == 0:
    divs.append(i)

ans = []
for i in range(N+1):
  for div in divs:
    if i % (N // div) == 0:
      ans.append(str(div))
      break
  else:
    ans.append("-")

print("".join(ans))

