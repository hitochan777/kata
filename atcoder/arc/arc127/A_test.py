N = int(input())

ans = 0
for i in range(1,N+1):
  for c in str(i):
    if c == "1":
      ans += 1
    else:
      break


print(ans)
