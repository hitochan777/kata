P = list(int(x) for x in input().split())

ans = ""
for p in P:
  ans += chr(ord('a') + p-1)

print(ans)