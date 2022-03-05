from collections import Counter
S = input()

cnt = Counter(S)

res = ""
for i in range(26):
  c = chr(i+ord("a"))
  res += c * cnt[c]

print(res)