cnt = {
  "v": 1,
  "w": 2
}
S = input()
ans = 0
for c in S:
  ans += cnt[c]
  
print(ans)