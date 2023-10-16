N, X = (int(x) for x in input().split())
s = ""
for i in range(26):
  s += chr(ord('A') + i) * N
  
print(s[X-1])